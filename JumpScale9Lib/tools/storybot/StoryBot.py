import time
import gevent
import signal

from .GithubBot import GithubBot
from .GiteaBot import GiteaBot

from js9 import j

TEMPLATE =  """
github_token_ = ""
github_repos = ""
gitea_api_url = "https://docs.greenitglobe.com/api/v1"
gitea_base_url = "https://docs.greenitglobe.com/"
gitea_token_ = ""
gitea_repos = ""
"""

JSConfigBase = j.tools.configmanager.base_class_config

class StoryBot(JSConfigBase):
    """
    Story bot will automaticall link story issues and task/bug/FR issues with each other.

    For more higher level information on the tool, check StoryBot.md
    """

    def __init__(self, instance, data=None, parent=None, interactive=False):
        """StoryBot constructor
        
        Keyword Arguments:
            data {data} -- StoryBot data matching the TEMPLATE(default: None)
        """

        JSConfigBase.__init__(self, instance=instance,
                                    data=data,
                                    parent=parent,
                                    template=TEMPLATE,
                                    interactive=interactive)

        # check configuration of the bot

    def run(self):
        """Run the StoryBot
        """
        gevent.signal(signal.SIGQUIT, gevent.kill)

        github_bot = None
        gitea_bot = None
        if self.config.data["github_repos"] != "":
            # create github bot
            token = self.config.data["github_token_"]
            repos = [item.strip() for item in self.config.data["github_repos"].split(",")]
            github_bot = GithubBot(token=token, repos=repos)

        if self.config.data["gitea_repos"] != "":
            # create gitea bot
            token = self.config.data["gitea_token_"]
            api_url = self.config.data["gitea_api_url"]
            base_url = self.config.data["gitea_base_url"]
            repos = [item.strip() for item in self.config.data["gitea_repos"].split(",")]
            gitea_bot = GiteaBot(token=token, api_url=api_url, base_url=base_url, repos=repos)

        # ask stories from bots
        start = time.time()
        gls = []
        if github_bot:
            gls.append(gevent.spawn(github_bot.get_stories))
        if gitea_bot:
            gls.append(gevent.spawn(gitea_bot.get_stories))

        # collect stories
        stories = []
        gevent.joinall(gls)
        for gl in gls:
            stories.extend(gl.value)
        end = time.time()
        self.logger.debug("Fetching stories took %ss" % (end-start))
        
        if not stories:
            self.logger.debug("No stories were found, skipping linking task to stories")
            return
        self.logger.debug("Found stories: %s", stories)

        # link task with stories with stories
        start = time.time()
        gls = []
        if github_bot:
            #github_bot.link_issues_to_stories(stories=stories)
            gls.append(gevent.spawn(github_bot.link_issues_to_stories, stories=stories))

        if gitea_bot:
            #github_bot.link_issues_to_stories(stories=stories)
            gls.append(gevent.spawn(gitea_bot.link_issues_to_stories, stories=stories))

        gevent.joinall(gls)
        end = time.time()
        self.logger.debug("Linking stories took %ss" % (end-start))

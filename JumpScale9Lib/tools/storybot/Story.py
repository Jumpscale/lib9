from .utils import _find_second

from js9 import j

class Story():
    """Represents a story
    """

    LIST_TITLE = "Stories"

    def __init__(self, title="", url="", description="", state="open", body="", update_list_func=None):
        """Constructor of a Story
        
        Keyword Arguments:
            title str -- title of the story (default: "")
            url str -- URL to the story issue (default: "")
            description str -- description of the story (default: "")
            state str -- state of the story ("open", "closed") (default: "open")
            body str -- Current body of the story issue (default: "")
            update_list_func func -- function that updates the task list on the story (default: None)
        
        Raises:
            ValueError -- if title was not provided
            ValueError -- if url was not provided
        """

        if title == "":
            raise ValueError("title was not provided and is mandatory")
        if url == "":
            raise ValueError("url was not provided and is mandatory")

        self.title = title
        self.url = url
        self.description = description
        self.state = state
        self.logger = j.logger.get("j.tools.StoryBot")
        self._body = body
        self._update_list_func = update_list_func

    def __repr__(self):
        return self.title

    def __eq__(self, other):
        return self.title == other

    @property
    def done_char(self):
        return "x" if self.state == "closed" else " "

    @property
    def md_item(self):
        """Returns the representation of the Story as a markdown list item
        
        Returns:
            str -- Story as mardown list item
        """
        return "- [%s] [%s: %s](%s)" % (self.done_char, self.title, self.description, self.url)

    def update_list(self, task):
        """Updated task list of story with provided task
        
        Arguments:
            task Task -- Task to add to Story
        """
        self._body = self._update_list_func(self._body, task)

    def index_in_body(self, body, start_i=0, end_i=-1):
        """Returns index of item in body
        Starting and ending from provided indexes

        Returns -1 if not found
        
        Arguments:
            body str -- issue body to look up the index of the task
        
        Keyword Arguments:
            start_i int -- Start index if lookup (default: 0)
            end_i int -- End index of lookup (default: -1)
        
        Raises:
            RuntimeError -- item could be wrongly formatted
        
        Returns:
            int -- line index of item in body
        """
        lines = body.splitlines()[start_i: end_i + 1 if end_i != -1 else None]
        for i, line in enumerate(lines, start=start_i):
            if i > end_i and not end_i < 0 :
                break
            # check if list item
            if not line.startswith("- ["):
                continue
            # get title from line and compare
            title_start = _find_second(line, char="[")
            if title_start == -1:
                self.logger.warning("List item is could be wrongly formatted: '%s'" % line)
            line_title = line[title_start: line.find(":")]
            if line_title == self.title:
                return i

        return -1

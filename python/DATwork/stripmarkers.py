def strip_comments(string, markers):
    lines = string.split('\n')
    for i in range(len(lines)):
        for marker in markers:
            pos = lines[i].find(marker)
            if pos != -1:
                lines[i] = lines[i][:pos]
        lines[i] = lines[i].rstrip()
    return '\n'.join(lines)


def solution(string,markers):
    lines = string.splitlines()
    for marker in markers:
        lines = [v.split(marker)[0].rstrip() if marker in v else v for v in lines]
    return '\n'.join(lines)


# print(solution('a #b\nc\nd $e f g', ['#', '$'])) # 'a\nc\nd'


import re

def strip_comments(text, comment_markers):
  """Strips all text that follows any of the given comment markers.

  Args:
    text: The text to strip comments from.
    comment_markers: A set of comment markers.

  Returns:
    The text with all comments stripped.
  """

  for marker in comment_markers:
    pattern = r'\s*{}.*'.format(re.escape(marker))
    text = re.sub(pattern, '', text, flags=re.M)

  return text.rstrip()


# print(strip_comments('a #b\nc\nd $e f g', ['#', '$'])) # 'a\nc\nd'

def strip_comments2(text, comment_markers):
    """
    Strip every line to the right of the comment markers, including the comment marker.

    Args:
        text (str): The text to strip comments from
        comment_markers (list): A list of comment markers (e.g. ['#', '//', '/*'])

    Returns:
        str: The text with comments stripped
    """
    import re
    text = re.sub(r'(?:^|\s)(' + '|'.join(comment_markers) + r')(?:\s|$)', '', text)
    return text

print(strip_comments2('a #b\nc\nd $e f g', ['#', '$'])) # 'a\nc\nd'
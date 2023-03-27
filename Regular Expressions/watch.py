#Suppose that you’d like to extract the URLs of YouTube videos that are embedded in pages
#(e.g., https://www.youtube.com/embed/xvFZjo5PgG0), converting them back to shorter,
#shareable youtu.be URLs (e.g., https://youtu.be/xvFZjo5PgG0) where they can be watched on YouTube itself.
#In a file called watch.py, implement a function called parse that expects a str of HTML as input,
#extracts any YouTube URL that’s the value of a src attribute of an iframe element therein, and returns its shorter,
# shareable youtu.be equivalent as a str. Expect that any such URL will be in one of the formats below.
#Assume that the value of src will be surrounded by double quotes. And assume that the input will contain no more than
#one such URL. If the input does not contain any such URL at all, return None.
# http://youtube.com/embed/xvFZjo5PgG0
# https://youtube.com/embed/xvFZjo5PgG0
# https://www.youtube.com/embed/xvFZjo5PgG0
#Structure watch.py as follows, wherein you’re welcome to modify main and/or implement other functions as you see fit,
#but you may not import any other libraries. You’re welcome, but not required, to use re and/or sys.


import re



def main():
    print(parse(input("HTML: ")))


def parse(s):
    s.strip()
    if matches := re.search(r"(https?://)?(www\.)?youtube.com/embed/([a-z0-9_]+)",s, re.IGNORECASE):
        #url re.sub(r"(https?://)?(www\.)?youtube.com/embed/", "https://youtu.be/", s)
        return "https://youtu.be/"+matches.group(3)
    else:
        return "None"

#Notice that the [a-z0-9_]+ tells the compiler to only expect a-z, 0-9, and _ as part of the regular
#expression. The + indicates that we are expecting one or more characters.
#For the purpose of tolerating both http and https, we add a ? to the end of https?, making the s optional.
#Further, to accommodate www we add (www\.)? to our code.
#Finally, just in case the user decides to leave out the protocol altogether, the http:// or https://
#is made optional using (https?://).


if __name__ == "__main__":
    main()
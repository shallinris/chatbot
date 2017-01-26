"""
This is the template server side for ChatBot
"""
from bottle import route, run, template, static_file, request
import json

swear_words = ['fuck', 'shit', 'damn', 'crap', 'asshole']
topics = ['dog', 'love', 'food', 'nature', 'fun', 'space']

@route('/', method='GET')
def index():
    return template("chatbot.html")


@route("/chat", method='POST')
def chat():
    user_message = request.POST.get('msg')

    if user_message[-1] =='?':
        return question_or_not(user_message)

    if any(x in user_message for x in topics):
        return fave_topics(user_message)

    if any(x in user_message for x in swear_words):
        return if_swear_word(user_message)

    return json.dumps({"animation": "money", "msg": user_message})

def question_or_not(input):
    question_response = "good question"
    question_response2 = "I have no idea"
    if input[-2:] == '??':
        return json.dumps({"animation": "afraid", "msg": question_response2})
    else:
        return json.dumps({"animation": "dancing", "msg": question_response})


def fave_topics(input):
    dog = ["dog"]
    flight = ["space"]
    message = "that is one of my favorite topics! ask me a question about it."
    if any(x in input for x in dog):
        return json.dumps({"animation": "dog", "msg": message})
    elif any(x in input for x in flight):
        return json.dumps({"animation": "takeoff", "msg": message})
    else:
        return json.dumps({"animation": "inlove", "msg": message})

def if_swear_word(input):
    bad_list = ['fuck face', 'shit hole', 'damn fucker','asshole wipe']
    ok_list = ['crap']
    swear_response = "it's not nice to swear"
    swear_response2 = "omg your mouth is dirty!"
    swear_response3 = "hehe that's not the worst swear word ever"
    if any(x in input for x in bad_list):
        return json.dumps({"animation": "no", "msg": swear_response2})
    elif any(x in input for x in ok_list):
        return json.dumps({"animation": "giggling", "msg": swear_response3})

    else:
        return json.dumps({"animation": "crying", "msg": swear_response})


@route("/test", method='POST')
def chat():
    user_message = request.POST.get('msg')
    return json.dumps({"animation": "inlove", "msg": user_message})

@route('/js/<filename:re:.*\.js>', method='GET')
def javascripts(filename):
    return static_file(filename, root='js')


@route('/css/<filename:re:.*\.css>', method='GET')
def stylesheets(filename):
    return static_file(filename, root='css')

@route('/images/<filename:re:.*\.(jpg|png|gif|ico)>', method='GET')
def images(filename):
    return static_file(filename, root='images')

def main():
    run(host='localhost', port=7002)

if __name__ == '__main__':
    main()

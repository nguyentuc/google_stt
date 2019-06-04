# -*- encoding: utf-8 -*-

def get_response(question):
    question = question.lower()
    if question == u'':
        return u'Xin lỗi, tôi không nghe thấy bạn nói gì.'
    else:
        return u'Nội dung:::"%s"' % (question)
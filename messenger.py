from flask import Blueprint, render_template, request, jsonify, redirect, url_for
import os
from User import User

messenger = Blueprint('messenger', 'messenger')


@messenger.route('/Messenger')
def load_messenger():

    user_id = request.cookies.get('user_id')
    _ = os.listdir(f'Messenger_records/{user_id}')
    people = [x[:-4] for x in _]
    print(people)
    return render_template("messengerForm.html", people=people, mensagens="")


@messenger.route('/Messenger', methods=['POST'])
def messenger_post():
    if request.form.get('searchPeople'):
        username = request.form.get('searchPeople')
        user_id = request.cookies.get('user_id')
        if os.path.exists(f'Messenger_records/{username}'):
            # TODO: throws error if user doesn't exist
            file = open(f'Messenger_records/{user_id}/{username}.txt', 'x')
            _ = os.listdir(f'Messenger_records/{user_id}')
            people = [x[:-4] for x in _]
            return render_template("messengerForm.html", people=people, mensagens="")
    elif request.form.get('personButton'):
        username = request.form.get('personButton')
        user_id = request.cookies.get('user_id')
        messages = []
        file = open(f'Messenger_records/{user_id}/{username}.txt', 'r')
        for m in file:
            x = m.split(':', 1)
            messages.append((x[0], x[1]))
        _ = os.listdir(f'Messenger_records/{user_id}')
        people = [x[:-4] for x in _]

        return render_template("messengerForm.html", people=people, mensagens=messages, currentPerson=username)

    elif request.form.get('message'):
        message = request.form.get('message')
        sender = request.cookies.get('user_id')
        to_send = request.form.get('to_send')

        file = open(f'Messenger_records/{sender}/{to_send}.txt', 'a')
        file.write(f'Sent:{message}\n')
        file.close()

        file2 = open(f'Messenger_records/{to_send}/{sender}.txt', 'a')
        file2.write(f'Received:{message}\n')
        file2.close()

        messages = []
        file = open(f'Messenger_records/{sender}/{to_send}.txt', 'r')
        for m in file:
            x = m.split(':', 1)
            messages.append((x[0], x[1]))
        _ = os.listdir(f'Messenger_records/{sender}')
        people = [x[:-4] for x in _]

        return render_template("messengerForm.html", people=people, mensagens=messages, currentPerson=to_send)
    # TODO: ATUALIZAR FORM DA PESSOA QUE RECEBEU A MENSAGEM, SE ESTA ESTIVER ONLINE NA PLATAFORMA






from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from flask_socketio import SocketIO, join_room
from os import path
from datetime import datetime

instantMessenger = Blueprint('instantMessenger', 'instantMessenger')


# ROUTES
@instantMessenger.route('/InstantMessenger')
def roomchoose():
    username = session.get('user_id')
    if username:
        return render_template('RoomChooseForm.html', username=username)


@instantMessenger.route('/InstantMessenger/Chat')
def listenroom():
    perm = False
    username = session.get('user_id')
    room = request.args.get('room')

    if username and room:
        if path.exists(f"/Room_Users/Room-{room}.txt"):
            file = open(f"Room_Users/Room-{room}.txt", "r")
            lines = file.readlines()
            for line in lines:
                if line == username:
                    perm = True
        else:
            message = 'Error: Chosen Room does not exist!'
            return render_template('RoomChooseForm.html', notice=message, username=username)
    else:
        return redirect(url_for('index'))

    file.close()

    if perm:
        return render_template('ChatForm.html', username=username, room=room)
    else:
        message = 'Error: You dont have permission to join this room!'
        return render_template('RoomChooseForm.html', notice=message, username=username)


@instantMessenger.route('/InstantMessenger/Subscribe')
def subscriberoom():
    username = session.get('user_id')
    room = request.args.get('sroom')

    if username and room:
        if path.exists(f"/Room_Users/Room-{room}.txt"):
            file = open(f"Room_Users/Room-{room}.txt", "w")
            file.write(username)
            file.close()

        else:
            message = 'Error: Chosen Room does not exist!'
            return render_template('RoomChooseForm.html', notice2=message, username=username)

    else:
        return redirect(url_for('index'))


@instantMessenger.route('/InstantMessenger/Unsubscribe')
def unsubscriberoom():
    username = session.get('user_id')
    room = request.args.get('uroom')

    if username and room:
        if path.exists(f"/Room_Users/Room-{room}.txt"):
            file = open(f"Room_Users/Room-{room}.txt", "w+")
            lines = file.readlines()
            for line in lines:
                if line == username:
                    line = line.replace(username, "")
                file.write(line)

        else:
            message = 'Error: Chosen Room does not exist!'
            return render_template('RoomChooseForm.html', notice2=message, username=username)

    else:
        return redirect(url_for('index'))

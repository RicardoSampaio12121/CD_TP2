from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from flask_socketio import SocketIO, join_room
import os
from datetime import datetime

instantMessenger = Blueprint('instantMessenger', 'instantMessenger')


# ROUTES


@instantMessenger.route('/InstantMessenger')
def instantmessenger():
    return render_template('RoomChooseForm.html')


@instantMessenger.route('/Chat')
def chat():
    username = request.cookies.get('user_id')
    room = request.args.get('room')

    if username and room:
        return render_template('ChatForm.html', username=username, room=room)
    else:
        return redirect(url_for('index.html'))


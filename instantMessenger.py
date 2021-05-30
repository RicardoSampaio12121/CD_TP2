from flask import Blueprint, render_template, request, jsonify, redirect, url_for, session
from flask_socketio import SocketIO, join_room
import os
from datetime import datetime

instantMessenger = Blueprint('instantMessenger', 'instantMessenger')


# ROUTES


@instantMessenger.route('/chat')
def chat():
    username = request.args.get('username')
    room = request.args.get('room')

    if username and room:
        return render_template('chat.html', username=username, room=room)
    else:
        return redirect(url_for('home'))



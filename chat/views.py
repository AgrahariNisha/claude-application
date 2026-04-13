from django.shortcuts import render, redirect, get_object_or_404
from .models import ChatSession, ChatMessage
from .services.ai_service import get_ai_response


def chat_home(request):
    sessions = ChatSession.objects.all().order_by('-created_at')

    # Create session if none
    session = sessions.first()
    if not session:
        session = ChatSession.objects.create(title="New Chat")

    messages = session.messages.all()

    return render(request, 'chat.html', {
        'sessions': sessions,
        'messages': messages,
        'current_session': session
    })


def chat_session(request, session_id):
    sessions = ChatSession.objects.all().order_by('-created_at')
    session = get_object_or_404(ChatSession, id=session_id)
    messages = session.messages.all()

    return render(request, 'chat.html', {
        'sessions': sessions,
        'messages': messages,
        'current_session': session
    })


def send_message(request, session_id):
    if request.method == "POST":
        user_msg = request.POST.get('message', '').strip()

        if not user_msg:
            return redirect('chat_session', session_id=session_id)

        session = get_object_or_404(ChatSession, id=session_id)

        # Save user message
        ChatMessage.objects.create(session=session, role='user', message=user_msg)

        # AI response
        ai_response = get_ai_response(user_msg)

        # Save AI message
        ChatMessage.objects.create(session=session, role='ai', message=ai_response)

    return redirect('chat_session', session_id=session_id)


def new_chat(request):
    session = ChatSession.objects.create(title="New Chat")
    return redirect('chat_session', session_id=session.id)


def clear_messages(request, session_id):
    session = get_object_or_404(ChatSession, id=session_id)
    session.messages.all().delete()
    return redirect('chat_session', session_id=session.id)
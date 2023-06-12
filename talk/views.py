from django.shortcuts import render, get_object_or_404, redirect
from item.models import Item
from .models import Talk
from .forms import TalkMessageForm

# Create your views here.
def new_talk(request, item_pk):
    item = get_object_or_404(Item, pk=item_pk)

    if item.created_by == request.user:
        return redirect('cart:index')

    talks = Talk.objects.filter(item=item).filter(members__in=[request.user.id]) 

    if talks:
        pass # redirect to talk

    if request.method == 'POST':
        form = TalkMessageForm(request.POST)

        if form.is_valid():
            talk = Talk.objects.create(item=item)
            talk.members.add(request.user)
            talk.members.add(item.created_by)
            talk.save() 

            talk_message = form.save(commit=False)
            talk_message.talk = talk
            talk_message.created_by = request.user
            talk_message.save() 

            return redirect('item:detail', pk=item_pk) 

    else:
        form = TalkMessageForm()

    return render(request, 'talk/new.html', {
        'form': form
    })            
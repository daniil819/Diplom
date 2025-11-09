from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import TableBookingForm


def table_booking(request):
    if not request.user.is_authenticated:
        messages.warning(request, 'Чтобы забронировать столик, пожалуйста, зарегистрируйтесь или войдите в систему.')
        return render(request, 'Order/table_booking.html')

    if request.method == 'POST':
        form = TableBookingForm(request.POST)
        if form.is_valid():
            booking = form.save(commit=False)
            booking.save()
            messages.success(request, 'Столик успешно забронирован! Мы свяжемся с вами для подтверждения.')
            return redirect('table_booking')
    else:
        form = TableBookingForm()

    return render(request, 'Order/table_booking.html', {'form': form})
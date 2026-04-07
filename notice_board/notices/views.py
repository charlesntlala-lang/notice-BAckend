from django.shortcuts import render, get_object_or_404, redirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.utils import timezone
from django.db.models import Q
from .models import Notice
from .forms import NoticeForm

def home(request):
    """Home page - list active notices with filters, pagination, sort. Admin toggle: active/upcoming/all."""
    # View mode for admins (active/upcoming/all)
    view_mode = request.GET.get('view_mode', 'active')
    now = timezone.now()
    
    # Base queryset based on view_mode
    notices = Notice.objects.all()
    if view_mode == 'active':
        notices = notices.filter(
            Q(publish_date__lte=now) | Q(publish_date__isnull=True),
            Q(expiry_date__gte=now) | Q(expiry_date__isnull=True)
        )
    elif view_mode == 'upcoming':
        notices = notices.filter(publish_date__gt=now)
    # 'all' shows everything without date filters

    # Filters
    category = request.GET.get('category', '')
    priority = request.GET.get('priority', '')
    from_date_str = request.GET.get('from_date', '')
    to_date_str = request.GET.get('to_date', '')
    
    if category:
        notices = notices.filter(category=category)
    if priority:
        notices = notices.filter(priority=priority)
    
    if from_date_str:
        from_date = timezone.datetime.strptime(from_date_str, '%Y-%m-%d')
        notices = notices.filter(created_at__gte=from_date)
    if to_date_str:
        to_date = timezone.datetime.strptime(to_date_str, '%Y-%m-%d')
        notices = notices.filter(created_at__lte=to_date)

    # Sort
    sort = request.GET.get('sort', '-created_at')
    notices = notices.order_by(sort)

    # Pagination
    paginator = Paginator(notices, 10)
    page_number = request.GET.get('page')
    notices_page = paginator.get_page(page_number)

    context = {
        'notices': notices_page,
        'categories': Notice.CATEGORY_CHOICES,
        'priorities': Notice.PRIORITY_CHOICES,
        'selected_category': category,
        'selected_priority': priority,
        'from_date': from_date_str,
        'to_date': to_date_str,
        'sort': sort,
        'view_mode': view_mode,
        'is_admin': request.user.is_staff,
    }
    return render(request, 'home.html', context)

def admin_required(user):
    return user.is_authenticated and user.is_staff

@login_required(login_url='/login/')
@user_passes_test(admin_required)
def admin_dashboard(request):
    now = timezone.now()
    notices = Notice.objects.filter(
        Q(publish_date__lte=now) | Q(publish_date__isnull=True),
        Q(expiry_date__gte=now) | Q(expiry_date__isnull=True)
    )[:10]
    context = {
        'notices': notices,
    }
    return render(request, 'admin_dashboard.html', context)

@login_required(login_url='/login/')
@user_passes_test(admin_required)
def notice_create(request):
    if request.method == 'POST':
        form = NoticeForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notice created successfully!')
            return redirect('notices:home')
    else:
        form = NoticeForm()
    return render(request, 'notice_form.html', {'form': form, 'action': 'Create'})

@login_required(login_url='/login/')
@user_passes_test(admin_required)
def notice_update(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        form = NoticeForm(request.POST, instance=notice)
        if form.is_valid():
            form.save()
            messages.success(request, 'Notice updated successfully!')
            return redirect('notices:home')
    else:
        form = NoticeForm(instance=notice)
    return render(request, 'notice_form.html', {'form': form, 'action': 'Update', 'notice': notice})

@login_required(login_url='/login/')
@user_passes_test(admin_required)
def notice_delete(request, pk):
    notice = get_object_or_404(Notice, pk=pk)
    if request.method == 'POST':
        notice.delete()
        messages.success(request, 'Notice deleted successfully!')
        return redirect('notices:home')
    return render(request, 'notice_confirm_delete.html', {'notice': notice})

def user_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Invalid credentials')
    return render(request, 'login.html')

def user_logout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('/')


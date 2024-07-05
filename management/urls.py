from django.urls import path 
from . import views

app_name = 'management'

urlpatterns = [

    path('', views.dashboard, name='dashboard'), #대쉬보드 화면
    path('detail/<int:id>/', views.detail, name='detail'), # 직원상세정보화면
    path('detail/<int:id>/edit', views.manager_edit, name='edit'), # 직원상세정보수정
    path('allow/', views.allow, name='allow'), #가입승인화면
    path('approve/<int:id>/', views.approve_user, name='approve_user'), #승인해주는 로직
    path('inactive/', views.inactive, name='inactive'), #퇴사 및 휴직 관리 화면
    path('disable/<int:id>/', views.disable, name='disable'), #비활성화 시킴
    path('active/<int:id>/', views.active, name='active'), #활성화 시킴
    path('leave_active/<int:id>/', views.leave_active, name='leave_active'), #휴직자로 변경
    path('retire_active/<int:id>/', views.retire_active, name='retire_active'), #퇴직자로 변경
    path('reject_active/<int:id>/', views.reject_active, name='reject_active'), #보류자로 변경
    path('test/', views.test, name='test'), #테스트
    path('search/', views.search, name='search'), #검색기능
]
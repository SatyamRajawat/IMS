from django.urls import path
from . import views


urlpatterns = [
    # path('index', views.index, name='index'),
    path('', views.home, name='home'),
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),

    path('admin/dept', views.add_dept, name='add_dept'),
    path('admin/dept/<slug:id>/change', views.change_dept, name='change_dept'),

    path('admin/class', views.add_classes, name='add_classes'),
    path('admin/class/<slug:id>/change',views.change_class, name='change_class'),

    
    path('admin/course',views.course, name='course'),
    path('admin/course/<slug:id>/change',views.course_update, name='course_update'),

    path('admin/student',views.add_student, name='add_student'),
    path('admin/student/<slug:id>/change',views.edit_student, name='edit_student'),

    path('admin/teacher',views.add_teacher, name='add_teacher'),
    path('admin/teacher/<slug:id>/change',views.edit_teacher, name='edit_teacher'),
    
    path('admin/assign',views.add_assign, name='add_assign'),
    path('admin/assign/<slug:id>/change',views.edit_assign, name='edit_assign'),

    path('student/<slug:stud_id>/attendance/', views.attendance, name='attendance'),



    


    path('student/<slug:stud_id>/attendance/', views.attendance, name='attendance'),
    path('student/<slug:stud_id>/<slug:course_id>/attendance/', views.attendance_detail, name='attendance_detail'),
    path('student/<slug:class_id>/timetable/', views.timetable, name='timetable'),
    # path('student/<slug:class_id>/search/', views.student_search, name='student_search'),

    path('student/<slug:stud_id>/marks_list/', views.marks_list, name='marks_list'),

    path('teacher/<slug:teacher_id>/<int:choice>/Classes/', views.t_clas, name='t_clas'),
    path('teacher/<int:assign_id>/Students/attendance/', views.t_student, name='t_student'),
    path('teacher/<int:assign_id>/ClassDates/', views.t_class_date, name='t_class_date'),
    path('teacher/<int:ass_c_id>/Cancel/', views.cancel_class, name='cancel_class'),
    path('teacher/<int:ass_c_id>/attendance/', views.t_attendance, name='t_attendance'),
    path('teacher/<int:ass_c_id>/Edit_att/', views.edit_att, name='edit_att'),
    path('teacher/<int:ass_c_id>/attendance/confirm/', views.confirm, name='confirm'),
    path('teacher/<slug:stud_id>/<slug:course_id>/attendance/', views.t_attendance_detail, name='t_attendance_detail'),
    path('teacher/<int:att_id>/change_attendance/', views.change_att, name='change_att'),
    path('teacher/<int:assign_id>/Extra_class/', views.t_extra_class, name='t_extra_class'),
    path('teacher/<slug:assign_id>/Extra_class/confirm/', views.e_confirm, name='e_confirm'),
    path('teacher/<int:assign_id>/Report/', views.t_report, name='t_report'),

    path('teacher/<slug:teacher_id>/t_timetable/', views.t_timetable, name='t_timetable'),
    path('teacher/<int:asst_id>/Free_teachers/', views.free_teachers, name='free_teachers'),

    path('teacher/<int:assign_id>/marks_list/', views.t_marks_list, name='t_marks_list'),
    path('teacher/<int:assign_id>/Students/Marks/', views.student_marks, name='t_student_marks'),
    path('teacher/<int:marks_c_id>/marks_entry/', views.t_marks_entry, name='t_marks_entry'),
    path('teacher/<int:marks_c_id>/marks_entry/confirm/', views.marks_confirm, name='marks_confirm'),
    path('teacher/<int:marks_c_id>/Edit_marks/', views.edit_marks, name='edit_marks'),

    

    # ================= Deleting ==========================

    path('admin/course/<slug:id>/delete', views.del_course, name='del_course'),
    path('admin/dept/<slug:id>/delete', views.del_dept, name='del_dept'),
    path('admin/class/<slug:id>/delete', views.del_class, name='del_class'),
    path('admin/student/<slug:id>/delete', views.del_student, name='del_student'),
    path('admin/teacher/<slug:id>/delete', views.del_teacher, name='del_teacher'),
    

    # ================= Checking ==========================

    path('check_dept', views.check_dept, name='check_dept'),
    path('check_class', views.check_class, name='check_class'),
    path('check_course', views.check_course, name='check_course'),
    path('check_student', views.check_student, name='check_student'),
    path('check_teacher', views.check_teacher, name='check_teacher'),






]
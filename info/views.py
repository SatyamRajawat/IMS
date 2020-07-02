from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from .models import Dept, Class, Student, Attendance, Course, Teacher, Assign, AttendanceTotal, time_slots, DAYS_OF_WEEK, AssignTime, AttendanceClass, StudentCourse, Marks, MarksClass
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.contrib.auth.models import auth
from django.contrib.auth import get_user_model
from django.contrib import messages
from django.shortcuts import redirect
from info.forms import *

User = get_user_model()
# Create your views here.

# ===================== Checking Duplicate ==================

def check_dept(request):
    if request.method=="GET":
        sn = request.GET['id']
        check = Dept.objects.filter(id=sn)       
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")

def check_class(request):
    if request.method=="GET":
        sn = request.GET['id']
        check = Class.objects.filter(id=sn)       
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")


def check_course(request):
    if request.method=="GET":
        sn = request.GET['id']
        check = Course.objects.filter(id=sn)       
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")

def check_student(request):
    if request.method=="GET":
        sn = request.GET['USN']
        check = Student.objects.filter(USN=sn)       
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")
def check_teacher(request):
    if request.method=="GET":
        sn = request.GET['id']
        check = Teacher.objects.filter(id=sn)       
        if len(check) == 1:
            return HttpResponse("Exists")
        else:
            return HttpResponse("Not Exists")

# def check_course(request):
#     if request.method=="GET":
#         sn = request.GET['id']
#         check = Course.objects.filter(id=sn)       
#         if len(check) == 1:
#             return HttpResponse("Exists")
#         else:
#             return HttpResponse("Not Exists")
# Deletion of objects====================================
def del_course(request,id):
    data =  Course.objects.get(id=id).delete()
    messages.success(request,'Course Deleted successfull!')
    return redirect('course')
def del_dept(request,id):
    data =  Dept.objects.filter(id=id).delete()
    messages.success(request,'Dept Deleted successfull!')
    return redirect('add_dept')

def del_class(request,id):
    data =  Class.objects.filter(id=id).delete()
    messages.success(request,'Class Deleted successfull!')
    return redirect('add_classes')
    
def del_student(request,id):
    data =  Student.objects.filter(USN=id).delete()
    messages.success(request,'Student Deleted successfull!')
    return redirect('add_student')

def del_teacher(request,id):
    data =  Teacher.objects.filter(id=id).delete()
    messages.success(request,'Teacher Deleted successfull!')
    return redirect('add_teacher')

    

# ================ ADD DEPARTMENT ========================

def add_dept(request):
    obj = Dept.objects.all()
    if request.method=='POST':
        frm=deptform(request.POST)
        if frm.is_valid:
            frm.save()
            messages.success(request,'Departement added Successfull !')
            return redirect('add_dept')
        else:
            messages.error(request,'Departement added Failed!!')
            return redirect('add_dept')
    else:
        frm=deptform()
    return render(request,'info/a_dept.html',{'dp':frm,'data':obj,'total':len(obj)}) 


def change_dept(request,id):
    data = Dept.objects.all().filter(id=id)
    obj2 = Class.objects.all().filter(dept_id=id)

    stu = Dept.objects.get(id=id)
    if request.method=='POST':
        print(request.POST)
        frm=deptform(request.POST,instance=stu)
        if frm.is_valid:
            frm.save()
            messages.success(request,'Departement Updated Successfull !')
            return redirect('add_dept')
        else:
            messages.error(request,'Departement added Failed!!')
            return redirect('change_dept')
    else:
        frm=classform()
    return render(request,'info/dept_change.html',{'ob':frm,'data1':data,'data2':obj2})

def add_classes(request):
    obj = Class.objects.all()
    if request.method=='POST':
        frm=classform(request.POST)
        if frm.is_valid:
            frm.save()
            messages.success(request,'Class Added Successfull!!')
            return redirect('add_classes')
            
        else:
            messages.Error(request,'Please Enter Valid Details')
            return render(request,'info/a_class.html',{'ob':frm,'data':obj})

    else:
        frm=classform() 
    return render(request,'info/a_class.html',{'ob':frm,'data':obj,'total':len(obj)})

def change_class(request,id):
    st = Student.objects.filter(class_id=id)
    obj= Class.objects.get(id=id)
    frm = studentform(request.POST or None)
    form = classform(request.POST or None, instance= obj)
    context= {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            messages.success(request, "You successfully updated the Class")
            return redirect('add_classes')
            
        else:
            frm = studentform()
            context= {'form': form}
            return render(request,'info/change_class.html',{'ob':form,'obj':obj})
    return render(request,'info/change_class.html',{'ob':form,'obj':obj,'st':st,'as':frm,'total':len(st)})


  
def course(request):
    data = Course.objects.all()
    if request.method =='POST':
        frm = courseform(request.POST)
        if frm.is_valid:
            frm.save()
            messages.success(request,'Course Added Successfull !')
            return redirect('course')

        else:
            messages.error(request,'Course Added Failed !')
            return redirect('course')
    else:
        frm=courseform
    return render(request,'info/course.html',{'ob':frm,'data':data})

def course_update(request,id):
    obj= Course.objects.get(id=id)
    print(obj)
    form = courseform(request.POST or None, instance= obj)
    context= {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            messages.success(request, "You successfully updated the Course")
            return redirect('course')
            
        else:
            context= {'form': form}
            return render(request,'info/course_up.html',{'ob':form,'obj':obj})
    return render(request,'info/course_up.html',{'ob':form,'obj':obj})
    

def add_student(request):
    st = Student.objects.all()
    form = studentform(request.POST or None)
    context= {'form': form}
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Student Added successfully!!")
            return redirect('add_student')
    
        else:
            us = request.POST['user']
            if Student.objects.filter(user_id=us).exists():
                sn = User.objects.get(id=us)
                messages.error(request, "Student {} Allready exists".format(sn))
                context= {'form': form}
                return render(request,'info/student.html',{'ob':form,'obj':st,'total':len(st)})

            else:
                messages.error(request, "Student Added Failed!!")
                context= {'form': form}
                return render(request,'info/student.html',{'ob':form,'obj':st,'total':len(st)})
    return render(request,'info/student.html',{'ob':form,'obj':st,'total':len(st)})

def edit_student(request,id):
    obj = Student.objects.get(USN=id)
    print(obj)
    form = studentform(request.POST or None, instance= obj)
    context= {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            messages.success(request, "Student Updated Successfully!!")
            return redirect('add_student')
            
        else:
            un = request.POST['user']
            if Student.objects.filter(user_id=un).exists():
                st = Student.objects.get(user_id=un)
                messages.error(request,'Student {} allready Exists'.format(st))
                context= {'form': form}
                return render(request,'info/edit_student.html',{'ob':form,'obj':obj})
    return render(request,'info/edit_student.html',{'ob':form,'obj':obj})


def add_teacher(request):
    st = Teacher.objects.all()
    form = teacherform(request.POST or None)
    context= {'form': form}
    if request.method == 'POST':
        print(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher Added successfully!!")
            return redirect('add_teacher')
    
        else:
            us = request.POST['user']
            if Teacher.objects.filter(user_id=us).exists():
                sn = User.objects.get(id=us)
                messages.error(request, "Techer {} Allready exists".format(sn))
                context= {'form': form}
                return render(request,'info/teacher.html',{'ob':form,'obj':st,'total':len(st)})

            else:
                messages.error(request, "Teacher Added Failed!!")
                context= {'form': form}
                return render(request,'info/teacher.html',{'ob':form,'obj':st,'total':len(st)})
    return render(request,'info/teacher.html',{'ob':form,'obj':st,'total':len(st)})

def edit_teacher(request,id):
    obj = Teacher.objects.get(id=id)
    form = teacherform(request.POST or None, instance= obj)
    context= {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            messages.success(request, "Techer Updated Successfully!!")
            return redirect('add_teacher')
            
        else:
            un = request.POST['user']
            if Student.objects.filter(user_id=un).exists():
                st = Student.objects.get(user_id=un)
                messages.error(request,'teacher {} allready Exists'.format(st))
                context= {'form': form}
                return render(request,'info/edit_teacher.html',{'ob':form,'obj':obj})
    return render(request,'info/edit_teacher.html',{'ob':form,'obj':obj})


def add_assign(request):
    st = Assign.objects.all()
    form = assignform(request.POST or None)
    context= {'form': form}
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            messages.success(request, "Teacher has assigned successfully!!")
            return redirect('add_assign')
        else:
            messages.error(request, "Teacher Assign Failed!!")
            context= {'form': form}
            return render(request,'info/assign.html',{'ob':form,'obj':st,'total':len(st)})
    return render(request,'info/assign.html',{'ob':form,'obj':st,'total':len(st)})

def edit_assign(request,id):
    data = AssignTime.objects.filter(assign_id=id)
    obj = Assign.objects.get(id=id)

    form = assignform(request.POST or None, instance= obj)
    context= {'form': form}

    form1 = timeform(request.POST or None)
    context= {'form1': form1}
    

    if request.method == 'POST':
        if form.is_valid():
            obj= form.save(commit= False)
            obj.save()
            messages.success(request, "Updated Successfully!!")
            return redirect('add_assign')
            
        else:
            messages.error(request, "Updation Failed!!")
            context= {'form': form}
            return render(request,'info/edit_assign.html',{'ob':form,'obj':obj,'ob1':form1})
    return render(request,'info/edit_assign.html',{'ob':form,'obj':obj ,'data':data,'ob1':form1})



# def add_time(request):
    # form = timeform(request.POST or None)
    # context= {'form': form}
    # if request.method == 'POST':
    #     print(request.POST)
    #     if form.is_valid():
    #         form.save()
    #         messages.success(request, "Tme has assigned successfully!!")
    #         return redirect('add_assign')
    #     else:
    #         messages.error(request, "Time Assign Failed!!")
    #         context= {'form': form}
    #         return render(request,'info/assign.html',{'ob1':form,'obj1':st})
#     return render(request,'info/assign.html',{'ob1':form,'obj1':st})





























def home(request):
    return render(request,'info/Home.html')

def signup(request):
    if request.method == 'POST':
        # first_name = request.POST['first_name']
        # last_name = request.POST['last_name']
        # email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 != password2:
            messages.error(request,'Error! Password and Confirm_password does not match')
            return redirect('/info/bas')

        user = User.objects.create_user(username=username, password=password1)
        user.save()
        messages.success(request,'User {} added Successfully'.format(username))

    # return render(request,'info/base.html')
    return HttpResponse('User Added Succesfull')


def signin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)

        if user is not None:
            auth.login(request,user)
            messages.success(request,'Successfull Login !!')
            return render(request, 'info/home.html')
        else:
            messages.error(request,'Invalid Credentials')
            return redirect('/info/home')
    
    else:
        return render(request,'home/base.html')

@login_required
def index(request):
    if request.user.is_staff:
        return render(request, 'info/t_homepage.html')
    if request.user.is_active:
        return render(request, 'info/homepage.html')
    return render(request, 'info/logout.html')

    






@login_required()
def attendance(request, stud_id):
    stud = Student.objects.get(USN=stud_id)
    ass_list = Assign.objects.filter(class_id_id=stud.class_id)
    att_list = []
    for ass in ass_list:
        try:
            a = AttendanceTotal.objects.get(student=stud, course=ass.course)
        except AttendanceTotal.DoesNotExist:
            a = AttendanceTotal(student=stud, course=ass.course)
            a.save()
        att_list.append(a)
    return render(request, 'info/attendance.html', {'att_list': att_list})


@login_required()
def attendance_detail(request, stud_id, course_id):
    stud = get_object_or_404(Student, USN=stud_id)
    cr = get_object_or_404(Course, id=course_id)
    att_list = Attendance.objects.filter(course=cr, student=stud).order_by('date')
    return render(request, 'info/att_detail.html', {'att_list': att_list, 'cr': cr})


# def student_search(request, class_id):
#     field = request.POST['fields']
#     search = request.POST['search']
#     class1 = get_object_or_404(Class, id=class_id)
#     if field == 'USN':
#         student_list = class1.student_set.filter(USN__icontains=search)
#     elif field == 'name':
#         student_list = class1.student_set.filter(name__icontains=search)
#     else:
#         student_list = class1.student_set.filter(sex__iexact=search)
#     return render(request, 'info/class1.html', {'class1': class1, 'student_list': student_list})


# Teacher Views

@login_required
def t_clas(request, teacher_id, choice):
    teacher1 = get_object_or_404(Teacher, id=teacher_id)
    return render(request, 'info/t_clas.html', {'teacher1': teacher1, 'choice': choice})


@login_required()
def t_student(request, assign_id):
    ass = Assign.objects.get(id=assign_id)
    att_list = []
    for stud in ass.class_id.student_set.all():
        try:
            a = AttendanceTotal.objects.get(student=stud, course=ass.course)
        except AttendanceTotal.DoesNotExist:
            a = AttendanceTotal(student=stud, course=ass.course)
            a.save()
        att_list.append(a)
    return render(request, 'info/t_students.html', {'att_list': att_list})


@login_required()
def t_class_date(request, assign_id):
    now = timezone.now()
    ass = get_object_or_404(Assign, id=assign_id)
    att_list = ass.attendanceclass_set.filter(date__lte=now).order_by('-date')
    return render(request, 'info/t_class_date.html', {'att_list': att_list})


@login_required()
def cancel_class(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    assc.status = 2
    assc.save()
    return HttpResponseRedirect(reverse('t_class_date', args=(assc.assign_id,)))


@login_required()
def t_attendance(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    ass = assc.assign
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
        'assc': assc,
    }
    return render(request, 'info/t_attendance.html', context)


@login_required()
def edit_att(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    cr = assc.assign.course
    att_list = Attendance.objects.filter(attendanceclass=assc, course=cr)
    context = {
        'assc': assc,
        'att_list': att_list,
    }
    return render(request, 'info/t_edit_att.html', context)


@login_required()
def confirm(request, ass_c_id):
    assc = get_object_or_404(AttendanceClass, id=ass_c_id)
    ass = assc.assign
    cr = ass.course
    cl = ass.class_id
    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.USN]
        if status == 'present':
            status = 'True'
        else:
            status = 'False'
        if assc.status == 1:
            try:
                a = Attendance.objects.get(course=cr, student=s, date=assc.date, attendanceclass=assc)
                a.status = status
                a.save()
            except Attendance.DoesNotExist:
                a = Attendance(course=cr, student=s, status=status, date=assc.date, attendanceclass=assc)
                a.save()
        else:
            a = Attendance(course=cr, student=s, status=status, date=assc.date, attendanceclass=assc)
            a.save()
            assc.status = 1
            assc.save()

    return HttpResponseRedirect(reverse('t_class_date', args=(ass.id,)))


@login_required()
def t_attendance_detail(request, stud_id, course_id):
    stud = get_object_or_404(Student, USN=stud_id)
    cr = get_object_or_404(Course, id=course_id)
    att_list = Attendance.objects.filter(course=cr, student=stud).order_by('date')
    return render(request, 'info/t_att_detail.html', {'att_list': att_list, 'cr': cr})


@login_required()
def change_att(request, att_id):
    a = get_object_or_404(Attendance, id=att_id)
    a.status = not a.status
    a.save()
    return HttpResponseRedirect(reverse('t_attendance_detail', args=(a.student.USN, a.course_id)))


@login_required()
def t_extra_class(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
    }
    return render(request, 'info/t_extra_class.html', context)


@login_required()
def e_confirm(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    cr = ass.course
    cl = ass.class_id
    assc = ass.attendanceclass_set.create(status=1, date=request.POST['date'])
    assc.save()

    for i, s in enumerate(cl.student_set.all()):
        status = request.POST[s.USN]
        if status == 'present':
            status = 'True'
        else:
            status = 'False'
        date = request.POST['date']
        a = Attendance(course=cr, student=s, status=status, date=date, attendanceclass=assc)
        a.save()

    return HttpResponseRedirect(reverse('t_clas', args=(ass.teacher_id,1)))


@login_required()
def t_report(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    sc_list = []
    for stud in ass.class_id.student_set.all():
        a = StudentCourse.objects.get(student=stud, course=ass.course)
        sc_list.append(a)
    return render(request, 'info/t_report.html', {'sc_list': sc_list})


@login_required()
def timetable(request, class_id):
    asst = AssignTime.objects.filter(assign__class_id=class_id)
    matrix = [['' for i in range(12)] for j in range(6)]

    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(12):
            if j == 0:
                matrix[i][0] = d[0]
                continue
            if j == 4 or j == 8:
                continue
            try:
                a = asst.get(period=time_slots[t][0], day=d[0])
                matrix[i][j] = a.assign.course_id
            except AssignTime.DoesNotExist:
                pass
            t += 1

    context = {'matrix': matrix}
    return render(request, 'info/timetable.html', context)


@login_required()
def t_timetable(request, teacher_id):
    asst = AssignTime.objects.filter(assign__teacher_id=teacher_id)
    class_matrix = [[True for i in range(12)] for j in range(6)]
    for i, d in enumerate(DAYS_OF_WEEK):
        t = 0
        for j in range(12):
            if j == 0:
                class_matrix[i][0] = d[0]
                continue
            if j == 4 or j == 8:
                continue
            try:
                a = asst.get(period=time_slots[t][0], day=d[0])
                class_matrix[i][j] = a
            except AssignTime.DoesNotExist:
                pass
            t += 1

    context = {
        'class_matrix': class_matrix,
    }
    return render(request, 'info/t_timetable.html', context)


@login_required()
def free_teachers(request, asst_id):
    asst = get_object_or_404(AssignTime, id=asst_id)
    ft_list = []
    t_list = Teacher.objects.filter(assign__class_id__id=asst.assign.class_id_id)
    for t in t_list:
        at_list = AssignTime.objects.filter(assign__teacher=t)
        if not any([True if at.period == asst.period and at.day == asst.day else False for at in at_list]):
            ft_list.append(t)

    return render(request, 'info/free_teachers.html', {'ft_list': ft_list})


# student marks


@login_required()
def marks_list(request, stud_id):
    stud = Student.objects.get(USN=stud_id,)
    ass_list = Assign.objects.filter(class_id_id=stud.class_id)
    sc_list = []
    for ass in ass_list:
        try:
            sc = StudentCourse.objects.get(student=stud, course=ass.course)
        except StudentCourse.DoesNotExist:
            sc = StudentCourse(student=stud, course=ass.course)
            sc.save()
            sc.marks_set.create(type='I', name='Internal test 1')
            sc.marks_set.create(type='I', name='Internal test 2')
            sc.marks_set.create(type='I', name='Internal test 3')
            sc.marks_set.create(type='E', name='Event 1')
            sc.marks_set.create(type='E', name='Event 2')
            sc.marks_set.create(type='S', name='Semester End Exam')
        sc_list.append(sc)

    return render(request, 'info/marks_list.html', {'sc_list': sc_list})


# teacher marks


@login_required()
def t_marks_list(request, assign_id):
    ass = get_object_or_404(Assign, id=assign_id)
    m_list = MarksClass.objects.filter(assign=ass)
    return render(request, 'info/t_marks_list.html', {'m_list': m_list})


@login_required()
def t_marks_entry(request, marks_c_id):
    mc = get_object_or_404(MarksClass, id=marks_c_id)
    ass = mc.assign
    c = ass.class_id
    context = {
        'ass': ass,
        'c': c,
        'mc': mc,
    }
    return render(request, 'info/t_marks_entry.html', context)


@login_required()
def marks_confirm(request, marks_c_id):
    mc = get_object_or_404(MarksClass, id=marks_c_id)
    ass = mc.assign
    cr = ass.course
    cl = ass.class_id
    for s in cl.student_set.all():
        mark = request.POST[s.USN]
        sc = StudentCourse.objects.get(course=cr, student=s)
        m = sc.marks_set.get(name=mc.name)
        m.marks1 = mark
        m.save()
    mc.status = True
    mc.save()

    return HttpResponseRedirect(reverse('t_marks_list', args=(ass.id,)))


@login_required()
def edit_marks(request, marks_c_id):
    mc = get_object_or_404(MarksClass, id=marks_c_id)
    cr = mc.assign.course
    stud_list = mc.assign.class_id.student_set.all()
    m_list = []
    for stud in stud_list:
        sc = StudentCourse.objects.get(course=cr, student=stud)
        m = sc.marks_set.get(name=mc.name)
        m_list.append(m)
    context = {
        'mc': mc,
        'm_list': m_list,
    }
    return render(request, 'info/edit_marks.html', context)


@login_required()
def student_marks(request, assign_id):
    ass = Assign.objects.get(id=assign_id)
    sc_list = StudentCourse.objects.filter(student__in=ass.class_id.student_set.all(), course=ass.course)
    return render(request, 'info/t_student_marks.html', {'sc_list': sc_list})












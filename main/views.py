from django.shortcuts import render
from .models import PersonalDetail, FamilyMember 
from .models import Education
def home(request):
    return render(request, 'main/home.html')
def personal_details(request):
    personal_data = PersonalDetail.objects.all()
    family = FamilyMember.objects.all()
    return render(request, 'main/personal_details.html', {
        'data': personal_data,
        'family': family,
    })
def education_view(request):
    education_data = Education.objects.prefetch_related('images').all()
    return render(request, 'main/education.html', {'education': education_data})
def personal_skills_view(request):
    skills = [
        {
            'title': 'Problem Solving',
            'description': 'Ability to break down complex problems and design efficient solutions using logic and creativity.',
            'image': 'https://cdn-icons-png.flaticon.com/512/3468/3468894.png',
        },
        {
            'title': 'Communication',
            'description': 'Clearly explaining ideas, writing documentation, and effectively collaborating in a team.',
            'image': 'https://cdn-icons-png.flaticon.com/512/2989/2989988.png',
        },
        {
            'title': 'Time Management',
            'description': 'Managing multiple projects and deadlines while staying productive and calm under pressure.',
            'image': 'https://cdn-icons-png.flaticon.com/512/4019/4019644.png',
        },
        {
            'title': 'Adaptability',
            'description': 'Keeping up with new tools, frameworks, and working in fast-paced tech environments.',
            'image': 'https://cdn-icons-png.flaticon.com/512/3653/3653050.png',
        },
        {
            'title': 'Team Collaboration',
            'description': 'Working effectively with developers, designers, and product teams toward a shared goal.',
            'image': 'https://cdn-icons-png.flaticon.com/512/4149/4149657.png',
        },
        {
            'title': 'Critical Thinking',
            'description': 'The ability to analyze problems deeply, evaluate options objectively, and make informed decisions in coding, debugging, and system design.',
            'image': 'https://cdn-icons-png.flaticon.com/512/2920/2920244.png',
        }
    ]
    return render(request, 'main/personal_skills.html', {'skills': skills})
def personal_projects_view(request):
    projects = [
        {
            'title': 'Quiz Game',
            'description': 'A clean, interactive web-based quiz app with multiple choice questions, scoring, and smooth UI using HTML, CSS & JS.',
            'image': '/static/main/img/quiz_game.png',
            'github': 'https://github.com/imcharan3/quiz_game',
        },
        {
            'title': 'Tic Tac Toe',
            'description': 'A responsive two-player Tic Tac Toe game with instant win logic and reset button built in HTML, CSS, and JavaScript.',
            'image': '/static/main/img/tic_tac_toe.png',
            'github': 'https://github.com/imcharan3/tic_tac_toe',
        }
    ]
    return render(request, 'main/personal_projects.html', {'projects': projects})
def internships_view(request):
    internships = [
        {
            'title': 'Data Analytics Internship',
            'organization': 'Aspire Primograd',
            'duration': '6 Weeks',
            'start_date': '16/06/2025',
            'description': 'A structured internship providing hands-on experience in front-end and back-end development, enhancing both technical and industry-relevant skills.',
            'contact': 'careerdesk@aspireprimograd.in',
            'status': 'Offer Accepted',
            'image': '/static/main/img/data_analytics_internship.png',  # 📸 Save a relevant icon here
        }
    ]
    return render(request, 'main/internships.html', {'internships': internships})

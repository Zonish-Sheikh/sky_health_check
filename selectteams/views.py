from django.shortcuts import render, redirect

def select_team(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        team = request.POST.get('team')
        print(f"Full Name: {full_name}, Team: {team}")
        return redirect('choose_team_cards')
    return render(request, 'select_team.html')

def choose_team_cards(request):
    if request.method == 'POST':
        selected_teams = request.POST.getlist('team')
        selected_cards = request.POST.getlist('card')

        if not selected_teams or not selected_cards:
            return render(request, 'choose_team_cards.html', {
                'error': 'Please select at least one team and one card!'
            })

        request.session['selected_teams'] = selected_teams
        request.session['selected_cards'] = selected_cards

        return redirect('view_selected_cards')

    return render(request, 'choose_team_cards.html')

def view_selected_cards(request):
    # Map of internal IDs to user-friendly names
    all_teams_map = {
        'team1': 'Team 1',
        'team2': 'Team 2',
        'team3': 'Team 3',
        'team4': 'Team 4',
        'team5': 'Team 5',
    }

    all_cards = [
        "Teamwork", "Support", "Pawns", "Mission",
        "Health of Codebase", "Suitable Process",
        "Delivering Value", "Learning", "Speed", "Fun/Easy"
    ]

    # Pull saved filters from session (from choose_team_cards page)
    selected_team_ids = request.session.get('selected_teams', list(all_teams_map.keys()))
    selected_cards = request.session.get('selected_cards', all_cards)

    # Translate team IDs to display names
    selected_teams = [all_teams_map.get(team_id, team_id) for team_id in selected_team_ids]

    return render(request, 'view_selected_cards.html', {
        'selected_teams': selected_teams,     # used for card rendering
        'selected_cards': selected_cards,     # used for card rendering
        'all_teams': list(all_teams_map.values()),  # used for generating checkboxes
        'all_cards': all_cards,               # used for generating checkboxes
    })


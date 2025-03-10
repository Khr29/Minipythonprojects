def display_activity(events):
    if not events:
        print("No recent activity found.")
        return
    
    print(f"\nRecent Activity for: {events[0]}['actor']['login']")
    print("-" * 45)

    for event in events[:5]:
        event_type = event['type'].replace("Event"," ")
        repo_name = event['repo']['name']
        print(f"✅ {event_type} in repo: {repo_name}")
    
    print("-" * 45)
import streamlit as st
import pandas as pd
import json
# ---------------------------
# Updated Questions Data
# ---------------------------

QUESTIONS = {}
# QUESTIONS = {
#     "Foodie Frenzy": [
#         {"points": 100, "question": "Which common kitchen ingredient is naturally radioactive due to high potassium-40 content?",
#          "options": ["A) Bananas", "B) Spinach", "C) Potatoes", "D) Brazil Nuts"], "answer": "D"},
        
#         {"points": 200, "question": "This illegal food contains live larvae and is banned in many countries. Name it!",
#          "image": "casu_marzu.jpg", "answer": "Casu Marzu cheese"},
        
#         {"points": 300, "question": "Which drink was banned for nearly a century due to myths about hallucinations?",
#          "options": ["A) Sake", "B) Absinthe", "C) Kombucha", "D) Pulque"], "answer": "B"},
        
#         {"points": 400, "question": "This sweet ingredient looks like glass under a microscope. What is it?",
#          "image": "sugar_microscope.jpg", "answer": "Sugar"},
        
#         {"points": 500, "question": "Which Japanese delicacy can kill you if not prepared by a licensed chef?",
#          "options": ["A) Natto", "B) Fugu", "C) Surströmming", "D) Basashi"], "answer": "B"}
#     ],
#     "Guess the Brand & Price": [
#         {"points": 100, "question": "This company, now known for sportswear, originally used a much more detailed logo before adopting its iconic swoosh. Name the brand.",
#          "image": "old_nike_logo.jpg", "answer": "Nike"},
        
#         {"points": 200, "question": "Which of these brands has a hidden arrow in its logo, symbolizing speed and precision?",
#          "options": ["A) FedEx", "B) Amazon", "C) Mercedes-Benz", "D) Toyota"], "answer": "A"},
        
#         {"points": 300, "question": "One of these watches is a luxury brand worth over $10,000, while the other costs under $200. Identify the luxury brand!",
#          "image": "rolex_vs_seiko.jpg", "answer": "Rolex"},
        
#         {"points": 400, "question": "What is the most expensive sneaker ever sold at an auction?",
#          "options": ["A) Nike Air Yeezy 1 (Kanye West Prototype)", "B) Michael Jordan’s Game-Worn Air Jordan 1s", 
#                      "C) Nike MAG Back to the Future Edition", "D) Solid Gold OVO x Air Jordans"], "answer": "A"},
        
#         {"points": 500, "question": "This car, a one-of-a-kind Bugatti, is the most expensive new car ever sold. How much did it cost?",
#          "image": "bugatti_la_voiture_noire.jpg",
#          "options": ["A) $8 million", "B) $12.5 million", "C) $18.7 million", "D) $25 million"], "answer": "C"}
#     ],
#     "Travel the World": [
#         {"points": 100, "question": "Which city is known as the ‘City of Gold’ due to its booming gold trade and luxurious lifestyle?", 
#          "image": "dubai_skyline.jpg", "answer": "Dubai"},
        
#         {"points": 200, "question": "Which city has the world’s busiest airport in terms of international passenger traffic?", 
#          "image": "dubai_airport.jpg", "answer": "Dubai"},
        
#         {"points": 300, "question": "In this country, it is illegal to wear high heels at certain historic sites to protect the ancient structures. Which country is it?", 
#          "image": "greece_acropolis.jpg", "answer": "Greece"},
        
#         {"points": 400, "question": "This country has a flag with a dragon on it, symbolizing its deep cultural and spiritual roots. Which country is it?", 
#          "image": "bhutan_flag.jpg", "answer": "Bhutan"},
        
#         {"points": 500, "question": "Which country has a town where the sun doesn’t set for around 4 months during summer and doesn’t rise for 4 months in winter?", 
#          "image": "svalbard_norway.jpg", "answer": "Norway (Svalbard)"}
#     ],
#     "How Well Do You Know Adi?": [
#         {"points": 100, "question": "What is Adi's favorite dessert?"},
#         {"points": 200, "question": "What is Adi's favorite chicken burger?"},
#         {"points": 300, "question": "Rank these fast food chains in Adi's order of preference: McDonald's, Domino's, Pizza Hut, Burger King."},
#         {"points": 400, "question": "What is Adi's favorite restaurant?"},
#         {"points": 500, "question": "What is Adi's favorite movie and favorite country other than India?"}
#     ],
#     "Mind-Bending Riddles": [
#         {"points": 100, "question": "I have 206 when I am grown, but only about 300 when I am born. What am I?"},
#         {"points": 200, "question": "I can be cracked, made, told, and played. What am I?"},
#         {"points": 300, "question": "If you drop me, I’m sure to crack, but smile at me, and I’ll smile back. What am I?"},
#         {"points": 400, "question": "I weigh nothing, but you can see me. If you put me in a bucket of water, the bucket becomes lighter. What am I?"},
#         {"points": 500, "question": "I exist in seconds, minutes, and centuries, but you will never find me in a day, week, or year. What am I?"}
#     ],
#     "Pop Culture & Entertainment": [
#         {"points": 100, "question": "This Tamil movie became India's official entry for the Oscars in 2023. Name it."},
#         {"points": 200, "question": "Identify this globally famous singer known for blending country and pop music.", "image": "taylor_swift.jpg"},
#         {"points": 300, "question": "This movie, based on real events, won multiple Oscars. Name it.", "image": "oppenheimer_scene.jpg"},
#         {"points": 400, "question": "Which Tamil movie holds the record for the highest box office collection worldwide?"},
#         {"points": 500, "question": "This sci-fi movie, released in the 2010s, became famous for its mind-bending plot and the concept of time inversion. Name it.", "image": "tenet_poster.jpg"}
#     ],
#     "TIE BREAKER": [
#         {"points": 100, "question": "This Tamil movie became India's official entry for the Oscars in 2023. Name it."},
#         {"points": 200, "question": "Identify this globally famous singer known for blending country and pop music.", "image": "taylor_swift.jpg"},
#         {"points": 300, "question": "This movie, based on real events, won multiple Oscars. Name it.", "image": "oppenheimer_scene.jpg"},
#         {"points": 400, "question": "Which Tamil movie holds the record for the highest box office collection worldwide?"},
#         {"points": 500, "question": "This sci-fi movie, released in the 2010s, became famous for its mind-bending plot and the concept of time inversion. Name it.", "image": "tenet_poster.jpg"}
#     ]
# }


# ---------------------------
# CSS for Animated Heading, Background, and Styles
# ---------------------------
st.markdown(
    """
    <style>
        /* Animated heading for JEOPARDY sign */
        @keyframes changeStyle {
            0%   { color: #ff4b4b; font-family: 'Courier New', Courier, monospace; }
            25%  { color: #4bff4b; font-family: 'Comic Sans MS', cursive, sans-serif; }
            50%  { color: #4b4bff; font-family: 'Georgia', serif; }
            75%  { color: #ff4bff; font-family: 'Impact', fantasy; }
            100% { color: #ff4b4b; font-family: 'Courier New', Courier, monospace; }
        }
        .animated-heading {
            animation: changeStyle 2s infinite;
            font-size: 4em;
            text-align: center;
            margin-bottom: 20px;
        }
        /* Gradient background */
        .stApp {
            background: linear-gradient(-45deg, #142850, #27496d, #00909e, #da22ff);
            background-size: 400% 400%;
            animation: smoothGradient 16s ease infinite;
            color: white;
            font-family: 'Arial', sans-serif;
        }
        @keyframes smoothGradient {
            0% { background-position: 0% 50%; }
            50% { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        /* Button styles for board boxes */
        .question-box {
            border: 2px solid #fff;
            border-radius: 8px;
            padding: 60px; /* Increased size */
            margin: 10px;
            text-align: center;
            cursor: pointer;
            font-size: 2.2em; /* Bigger font */
            width: 150px; /* Adjust box width */
            height: 100px; /* Adjust box height */
            display: flex;
            align-items: center;
            justify-content: center;
        }
        .done {
            background-color: #2ecc71;  /* green */
            color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)


import streamlit as st
import json
import pandas as pd

# ---------------------------
# Initialize Session State
# ---------------------------
if "teams" not in st.session_state:
    st.session_state.teams = ["Team A", "Team B", "Team C", "Team D"]
if "scores" not in st.session_state:
    st.session_state.scores = {team: 0 for team in st.session_state.teams}
if "page" not in st.session_state:
    st.session_state.page = "setup"
if "current_question" not in st.session_state:
    st.session_state.current_question = {}
if "QUESTIONS" not in st.session_state:
    st.session_state.QUESTIONS = {}
if "answered" not in st.session_state:
    st.session_state.answered = {}

# ---------------------------
# Navigation Functions
# ---------------------------
def go_to_board():
    st.session_state.page = "board"
    st.rerun()

def go_to_question(category, points, question_text):
    st.session_state.current_question = {"category": category, "points": points, "question": question_text}
    st.session_state.page = "question"
    st.rerun()

def update_score(team, pts):
    st.session_state.scores[team] += pts
    st.session_state.answered[(st.session_state.current_question["category"], st.session_state.current_question["points"])] = True
    go_to_board()

# ---------------------------
# Setup Page
# ---------------------------
if st.session_state.page == "setup":
    st.title("Setup Game")

    rules_text = """Jeopardy Game Rules and Questions File Format Instructions

    HINT:JUST COPY PASTE THIS IN CHATGPT AND YOUR QUESTIONS,POINTS AND TOPICS AND IT WILL FORMAT IT FOR YOU! (you will put the json in a 
    seperate text file and upload in the website.)

    GAME RULES:
    1. Each team takes turns selecting a question.
    2. Answer correctly to earn the specified points; incorrect answers may result in point deductions.
    3. Some questions include multiple-choice options for reference.
    4. If no team knows the answer, use the "No One Knows the Answer" option.
    5. Negative marking may apply to specific questions.
    6. The host's decision is final. Have fun!

    QUESTIONS FILE FORMAT:
    Your questions file must be a valid JSON file with the following structure:

    {
    "Topic Name": [
    {"points": 100, "question": "Your question here", "options": ["Option A", "Option B", "Option C", "Option D"], "answer": "Correct Answer"},
    {"points": 200, "question": "Your question here", "options": [], "answer": "Correct Answer"},
    {"points": 300, "question": "Your question here", "options": [], "answer": "Correct Answer"},
    {"points": 400, "question": "Your question here", "options": [], "answer": "Correct Answer"},
    {"points": 500, "question": "Your question here", "options": [], "answer": "Correct Answer"}
    ]
    }

    EXAMPLE QUESTIONS FILE:
    {
    "Foodie Frenzy": [
        {"points": 100, "question": "Which common kitchen ingredient is naturally radioactive due to high potassium-40 content?",
        "options": ["A) Bananas", "B) Spinach", "C) Potatoes", "D) Brazil Nuts"], "answer": "D"},
            
        {"points": 200, "question": "This illegal food contains live larvae and is banned in many countries. Name it!",
        "image": "casu_marzu.jpg", "answer": "Casu Marzu cheese"},
            
        {"points": 300, "question": "Which drink was banned for nearly a century due to myths about hallucinations?",
        "options": ["A) Sake", "B) Absinthe", "C) Kombucha", "D) Pulque"], "answer": "B"},
            
        {"points": 400, "question": "This sweet ingredient looks like glass under a microscope. What is it?",
        "image": "sugar_microscope.jpg", "answer": "Sugar"},
            
        {"points": 500, "question": "Which Japanese delicacy can kill you if not prepared by a licensed chef?",
        "options": ["A) Natto", "B) Fugu", "C) Surströmming", "D) Basashi"], "answer": "B"}
    ],
    "Guess the Brand & Price": [
        {"points": 100, "question": "This company, now known for sportswear, originally used a much more detailed logo before adopting its iconic swoosh. Name the brand.",
        "image": "old_nike_logo.jpg", "answer": "Nike"},
            
        {"points": 200, "question": "Which of these brands has a hidden arrow in its logo, symbolizing speed and precision?",
        "options": ["A) FedEx", "B) Amazon", "C) Mercedes-Benz", "D) Toyota"], "answer": "A"}
    ],
    "Travel the World": [
        {"points": 100, "question": "Which city is known as the ‘City of Gold’ due to its booming gold trade and luxurious lifestyle?", 
        "image": "dubai_skyline.jpg", "answer": "Dubai"}
    ]
    }
    """

    st.download_button(
        label="📄 Download Game Rules and JSON Template",
        data=rules_text,
        file_name="jeopardy_rules.txt",
        mime="text/plain"
    )


    # Upload Questions File
    uploaded_file = st.file_uploader("Upload Questions File (TXT format)", type=["txt"])
    
    if uploaded_file:
        raw_text = uploaded_file.getvalue().decode("utf-8")
        try:
            st.session_state.QUESTIONS = json.loads(raw_text)
            st.session_state.answered = {(cat, q["points"]): False for cat in st.session_state.QUESTIONS for q in st.session_state.QUESTIONS[cat]}
            st.success("Questions loaded successfully!")
        except json.JSONDecodeError:
            st.error("Invalid file format. Ensure the file contains a valid JSON structure.")

    # Setup Teams
    num_teams = st.number_input("Number of Teams", min_value=1, max_value=10, value=len(st.session_state.teams))
    teams = []
    for i in range(int(num_teams)):
        default_name = st.session_state.teams[i] if i < len(st.session_state.teams) else f"Team {i+1}"
        team_name = st.text_input(f"Team {i+1} Name", value=default_name, key=f"team_{i}")
        teams.append(team_name)

    if st.button("Start Game"):
        st.session_state.teams = teams
        st.session_state.scores = {team: 0 for team in teams}
        st.session_state.page = "board"
        st.rerun()

# ---------------------------
# Board Page
# ---------------------------
if st.session_state.page == "board":
    st.markdown("<div class='animated-heading'>JEOPARDY</div>", unsafe_allow_html=True)
    st.title("Birthday Jeopardy")

    # Ensure questions are loaded
    if not st.session_state.QUESTIONS:
        st.error("No questions loaded! Please upload a file on the setup page.")
        if st.button("Go Back to Setup"):
            st.session_state.page = "setup"
            st.rerun()
        st.stop()

    # Leaderboard Table
    leaderboard_data = [{"Team": team, "Points": pts} for team, pts in st.session_state.scores.items()]
    df = pd.DataFrame(leaderboard_data).sort_values(by="Points", ascending=False).reset_index(drop=True)
    
    medals = ["🥇", "🥈", "🥉"]
    df["Team"] = [f"{medals[i]} {team}" if i < 3 else team for i, team in enumerate(df["Team"])]
    st.subheader("🏆 Leaderboard 🏆")
    st.dataframe(df, hide_index=True)

    st.markdown("## Select a Question")
    for category, questions in st.session_state.QUESTIONS.items():
        st.markdown(f"### {category}")
        cols = st.columns(min(len(questions), 5))
        for idx, q in enumerate(questions):
            points = q["points"]
            question_text = q["question"]
            answered = st.session_state.answered[(category, points)]
            btn_label = f"✅ {points}" if answered else f"{points}"
            if cols[idx % 5].button(btn_label, key=f"{category}_{points}", help=question_text):
                if not answered:
                    go_to_question(category, points, question_text)
    
    if st.button("Reset Game 🔄"):
        st.session_state.scores = {team: 0 for team in st.session_state.scores}
        st.session_state.answered = {(cat, q["points"]): False for cat in st.session_state.QUESTIONS for q in st.session_state.QUESTIONS[cat]}
        st.rerun()

    st.markdown("### ✏️ Manually Edit Scores")
    for team in st.session_state.scores:
        new_score = st.number_input(f"{team} Score:", value=st.session_state.scores[team], step=50, key=f"edit_{team}")
        if st.button(f"Update {team} Score", key=f"update_{team}"):
            st.session_state.scores[team] = new_score
            st.success(f"{team} score updated to {new_score}!")

    if st.button("Back to Setup"):
        st.session_state.page = "setup"
        st.rerun()

    st.stop()

# ---------------------------
# Question Page
# ---------------------------
# Ensure QUESTIONS is initialized before anything else
if "QUESTIONS" not in st.session_state:
    st.session_state.QUESTIONS = {}

if st.session_state.page == "question":
    current = st.session_state.current_question
    category, points, question_text = current["category"], current["points"], current["question"]

    st.markdown("<div class='animated-heading'>JEOPARDY</div>", unsafe_allow_html=True)
    st.title(f"{category} - {points} Points")
    st.markdown(f"<p style='font-size:2em;'>Question: {question_text}</p>", unsafe_allow_html=True)
    
    # Check if the category exists before accessing it
    if category in st.session_state.QUESTIONS:
        question_list = st.session_state.QUESTIONS[category]
        matching_questions = [q for q in question_list if q["points"] == points]

        if matching_questions:
            question_data = matching_questions[0]

            # If the question has multiple-choice options, display them
            if "options" in question_data:
                options = question_data.get("options", [])
                st.markdown("**Options:**")
                for opt in options:
                    st.markdown(f"- {opt}")
        else:
            st.error("No matching question found for the selected points.")
    else:
        st.error(f"Category '{category}' not found in the questions.")

    st.markdown("### Award Points")
    teams = st.session_state.teams

    # Full points buttons
    st.markdown("#### Full Points")
    full_cols = st.columns(len(teams))
    for idx, team in enumerate(teams):
        if full_cols[idx].button(f"{team} +{points}", key=f"full_{team}_{category}_{points}"):
            update_score(team, points)

    # Half points buttons
    st.markdown("#### Half Points")
    half_cols = st.columns(len(teams))
    half_points = points // 2
    for idx, team in enumerate(teams):
        if half_cols[idx].button(f"{team} +{half_points}", key=f"half_{team}_{category}_{points}"):
            update_score(team, half_points)

    # Button for when no one knows the answer
    if st.button("No One Knows the Answer"):
        st.session_state.answered[(category, points)] = True
        go_to_board()

    # Custom Negative Marking
    st.markdown("### Apply Negative Marking")
    neg_points = st.number_input("Enter Negative Points:", min_value=1, step=1, value=50)

    neg_cols = st.columns(len(teams))
    for idx, team in enumerate(teams):
        if neg_cols[idx].button(f"{team} -{neg_points}", key=f"neg_{team}_{category}_{points}"):
            st.session_state.scores[team] -= neg_points
            go_to_board()

    # Option to go back without awarding
    if st.button("Back to Board"):
        go_to_board()

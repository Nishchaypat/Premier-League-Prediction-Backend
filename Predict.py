import tkinter as tk
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
from sklearn.impute import SimpleImputer
from sklearn.svm import SVC

class FootballMatchPredictionApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Create widgets
        self.home_team_label = tk.Label(self, text="Home team:")
        self.home_team_entry = tk.Entry(self)
        self.away_team_label = tk.Label(self, text="Away team:")
        self.away_team_entry = tk.Entry(self)
        self.predict_button = tk.Button(self, text="Predict", command=self.predict_winner)
        self.result_label = tk.Label(self, text="")

        # Place widgets
        self.home_team_label.grid(row=0, column=0)
        self.home_team_entry.grid(row=0, column=1)
        self.away_team_label.grid(row=1, column=0)
        self.away_team_entry.grid(row=1, column=1)
        self.predict_button.grid(row=2, column=0)
        self.result_label.grid(row=2, column=1)

    def predict_winner(self):
        home_team = self.home_team_entry.get()
        away_team = self.away_team_entry.get()

        result = predict_winner(home_team, away_team)

        self.result_label.config(text=result)

def predict_winner(home_team, away_team):
  home_name=home_team
  away_name=away_team
  import pandas as pd
    # ... (your existing prediction code)
  for k,v in number_to_string_mapping.items():
      if home_name == v:
          home_name = k
      if away_name == v:
          away_name = k
  
  team_data = df[(df['Home_Team'] == home_name) | (df['Away_Team'] == away_name)]
  home_team_data = df[df['Home_Team'] == home_name]
  away_team_data = df[df['Away_Team'] == away_name]

  # Calculate mean values for all features for the specified team
  mean_home_shots = home_team_data['Home_Shots'].mean()
  mean_away_shots = away_team_data['Away_Shots'].mean()
  mean_home_shots_on_target = home_team_data['Home_Shots_on_Target'].mean()
  mean_away_shots_on_target = away_team_data['Away_Shots_on_Target'].mean()
  mean_home_fouls = home_team_data['Home_Fouls'].mean()
  mean_away_fouls = away_team_data['Away_Fouls'].mean()
  mean_home_corners = home_team_data['Home_Corners'].mean()
  mean_away_corners = away_team_data['Away_Corners'].mean()
  mean_home_yellow_cards = home_team_data['Home_Yellow_Cards'].mean()
  mean_away_yellow_cards = away_team_data['Away_Yellow_Cards'].mean()
  mean_home_red_cards = home_team_data['Home_Red_Cards'].mean()
  mean_away_red_cards = away_team_data['Away_Red_Cards'].mean()
  mean_bet_of_away_team_winning = team_data['bet_of_away_team_winning'].mean()
  mean_bet_for_draw = team_data['bet_for_draw'].mean()
  mean_bet_of_home_team_winning = home_team_data['bet_of_home_team_winning'].mean()

  # Prepare data for the match you want to predict with mean values
  match_data = pd.DataFrame({
      "Home_Team" : [home_name],
      "Away_Team" : [away_name],
      'Home_Shots': [mean_home_shots],  # Add these missing features
      'Away_Shots': [mean_away_shots],
      'Home_Shots_on_Target': [mean_home_shots_on_target],
      'Away_Shots_on_Target': [mean_away_shots_on_target],
      'Home_Fouls': [mean_home_fouls],
      'Away_Fouls': [mean_away_fouls],
      'Home_Corners': [mean_home_corners],
      'Away_Corners': [mean_away_corners],
      'Home_Yellow_Cards': [mean_home_yellow_cards],
      'Away_Yellow_Cards': [mean_away_yellow_cards],
      'Home_Red_Cards': [mean_home_red_cards],
      'Away_Red_Cards': [mean_away_red_cards],
      'bet_of_away_team_winning': [mean_bet_of_away_team_winning],
      'bet_for_draw': [mean_bet_for_draw],
      'bet_of_home_team_winning': [mean_bet_of_home_team_winning]
  })
  # Make prediction
  result = svm_classifier.predict(match_data)

  # Return prediction
  if result == 'H':
      return f"{home_team} is predicted to win."
  elif result == 'A':
      return f"{away_team} is predicted to win."
  else: 
        return "The match is predicted to be a draw."

  return result

if __name__ == "__main__":
  df = pd.read_csv("Main.csv")
  df = df.drop("Unnamed: 0", axis=1)
  
  from sklearn.model_selection import train_test_split
  from sklearn.preprocessing import LabelEncoder
  from sklearn.metrics import accuracy_score, classification_report, confusion_matrix
  from sklearn.impute import SimpleImputer
  from sklearn.svm import SVC


  df = pd.read_csv("Main.csv")
  df = df.drop("Unnamed: 0", axis =1)
  df.rename(columns={
      'HomeTeam': 'Home_Team',
      'AwayTeam': 'Away_Team',
      'sum_of_home': 'bet_of_away_team_winning',
      'sum_of_draw': 'bet_for_draw',
      'sum_of_away': 'bet_of_home_team_winning',
      'HS': 'Home_Shots',
      'AS': 'Away_Shots',
      'HST': 'Home_Shots_on_Target',
      'AST': 'Away_Shots_on_Target',
      'HF': 'Home_Fouls',
      'AF': 'Away_Fouls',
      'HC': 'Home_Corners',
      'AC': 'Away_Corners',
      'HY': 'Home_Yellow_Cards',
      'AY': 'Away_Yellow_Cards',
      'HR': 'Home_Red_Cards',
      'AR': 'Away_Red_Cards',
      'FTR' : 'Final_Game_Result'
  }, inplace=True)


  numeric_columns = df.select_dtypes(exclude=['object'])

  df[numeric_columns.columns] = df[numeric_columns.columns].fillna(df[numeric_columns.columns].mean())

  label_encoder = LabelEncoder()
  df['Home_Team'] = label_encoder.fit_transform(df['Home_Team'])
  df['Away_Team'] = label_encoder.transform(df['Away_Team'])

  X = df.drop(['Final_Game_Result'], axis=1)
  y = df['Final_Game_Result']


  X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)


  imputer = SimpleImputer(strategy='mean')
  X_train = imputer.fit_transform(X_train)
  X_test = imputer.transform(X_test)


  svm_classifier = SVC(kernel='linear', C=1.0, random_state=42)
  svm_classifier.fit(X_train, y_train)

  y_pred = svm_classifier.predict(X_test)

  accuracy = accuracy_score(y_test, y_pred)
  confusion = confusion_matrix(y_test, y_pred)
  classification_rep = classification_report(y_test, y_pred)

  print("Accuracy:", accuracy)
  print("Confusion Matrix:\n", confusion)
  print("Classification Report:\n", classification_rep)


  unique_teams = pd.concat([df["Home_Team"], df["Away_Team"]]).unique()

  team_list = unique_teams.tolist()

  number_to_string_mapping = {i: team for i, team in enumerate(label_encoder.classes_)}


  svm_classifier = SVC(kernel='linear', C=1.0, random_state=42)
  svm_classifier.fit(X_train, y_train)

  app = FootballMatchPredictionApp()
  app.mainloop()

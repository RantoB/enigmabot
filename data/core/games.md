## présentation des jeux
* question_pitch
  - action_which_game
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"} OR meurtre_krutenau{"game": "Meurtre à la Krutenau"}
 - action_requested_game
* deny OR affirm
  - action_next_game

## présentation jeu 1
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"}
  - utter_societe_musterieuse
  - utter_next_game
* deny OR affirm
  - action_next_game

## présentation jeu 2
* meurtre_krutenau{"game": "Meurtre à la Krutenau"}
  - utter_meurtre_krutenau
  - utter_next_game
* deny OR affirm
  - action_next_game

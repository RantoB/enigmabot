## présentation des jeux
> check_if_question_or_deny
* question_pitch
  - action_check_active_form
  - action_which_game
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"} OR meurtre_krutenau{"game": "Meurtre à la Krutenau"}
 - action_requested_game
* deny OR affirm
  - action_next_game
> check_answer_about_ENIGMA_Stras

## présentation jeu 1
> check_if_question_or_deny
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"}
  - action_check_active_form
  - utter_societe_mysterieuse
  - utter_next_game
* deny OR affirm
  - action_next_game
> check_answer_about_ENIGMA_Stras

## présentation jeu 2
> check_if_question_or_deny
* meurtre_krutenau{"game": "Meurtre à la Krutenau"}
  - action_check_active_form
  - utter_meurtre_krutenau
  - utter_next_game
* deny OR affirm
  - action_next_game
> check_answer_about_ENIGMA_Stras

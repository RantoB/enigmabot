## greet and 2 riddles no3 (/tmp/tmp546s3d11/92f94d04ec714373a208e8ea80ca5633_test_stories.md)
* inform_kind_of_riddle: pose moi une charade   <!-- predicted: inform_kind_of_riddle: pose moi une [charade](riddle_category)[charade](riddle_category) -->
    - slot{"riddle_category": "charade"}
    - form_riddle   <!-- predicted: action_default_fallback -->
    - form{"name": "form_riddle"}
    - form{"name": null}
    - utter_propose_riddle
* affirm: ok
    - form_riddle
    - form{"name": "form_riddle"}
    - form{"name": null}
    - utter_propose_riddle
* deny: no
    - utter_question_on_ENIGMA_Stras
* deny: non
    - utter_subscribe
* deny: no
    - utter_thanks
    - utter_goodbye
* goodbye: ciao
    - utter_goodbye


## subscribe and pitch question (/tmp/tmp546s3d11/92f94d04ec714373a208e8ea80ca5633_test_stories.md)
* how_to_subscribe: j'aimerais recevoir la newsletter
    - form_subscribe
    - form_subscribe
    - form{"name": null}
* affirm: oui
    - action_save_information
    - utter_question_on_ENIGMA_Stras
* affirm: oui
    - utter_question
* question_pitch: quels sont les jeux
    - action_which_game
* societe_mysterieuse: C'est quoi  société mystérieuse de Strasbourg   <!-- predicted: societe_mysterieuse: C'est quoi  [société mystérieuse de Strasbourg](game)[société mystérieuse de Strasbourg](game) -->
    - slot{"game": "société mystérieuse de Strasbourg"}
    - action_requested_game
* affirm: wé
    - action_next_game
* deny: no
    - utter_propose_riddle
* deny: nan
    - utter_thanks   <!-- predicted: utter_subscribe -->
    - utter_goodbye
* goodbye: ciao
    - utter_goodbye



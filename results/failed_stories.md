## greet and 2 riddles no1 (/tmp/tmpvvzewwcn/708924ba52384104a6f4e4549c8ceed0_test_stories.md)
* greet: hello
    - utter_greet_and_propose_riddle   <!-- predicted: utter_greet -->
* affirm: oui
    - form_riddle
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
    - utter_thanks   <!-- predicted: utter_propose_riddle -->
    - utter_goodbye
* goodbye: ciao


## greet and 2 riddles no2 (/tmp/tmpvvzewwcn/708924ba52384104a6f4e4549c8ceed0_test_stories.md)
* greet: hello
    - utter_greet
* ask_for_riddle: t'aurais une bonne énigme ?
    - form_riddle
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
    - utter_thanks   <!-- predicted: utter_propose_riddle -->
    - utter_goodbye
* goodbye: ciao


## greet and 2 riddles no3 (/tmp/tmpvvzewwcn/708924ba52384104a6f4e4549c8ceed0_test_stories.md)
* inform_kind_of_riddle: tu connais une charade ?   <!-- predicted: inform_kind_of_riddle: tu connais une [charade](riddle_category) ? -->
    - slot{"riddle_category": "charade"}
    - form_riddle
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
    - utter_thanks   <!-- predicted: utter_propose_riddle -->
    - utter_goodbye
* goodbye: ciao


## greet and 2 faq no1 (/tmp/tmpvvzewwcn/708924ba52384104a6f4e4549c8ceed0_test_stories.md)
* greet: bonjour
    - utter_greet
* faq: combien ça coûte ?
    - action_set_faq_slot
    - respond_faq
    - utter_one_more_question
* faq: Combien de temps est-ce que ça dure ?
    - action_set_faq_slot
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle   <!-- predicted: utter_thanks -->
* deny: non
    - utter_before_end   <!-- predicted: utter_question_on_ENIGMA_Stras -->
    - utter_goodbye   <!-- predicted: action_listen -->
* goodbye: a bientôt
    - action_listen   <!-- predicted: utter_thanks -->


## greet and 2 faq no2 (/tmp/tmpvvzewwcn/708924ba52384104a6f4e4549c8ceed0_test_stories.md)
* greet: bonjour
    - utter_greet
* affirm: oui
    - utter_question   <!-- predicted: form_riddle -->
* faq: combien ça coûte ?
    - action_set_faq_slot
    - respond_faq
    - utter_one_more_question
* faq: Combien de temps est-ce que ça dure ?
    - action_set_faq_slot
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle   <!-- predicted: utter_thanks -->
* deny: non
    - utter_before_end   <!-- predicted: utter_question_on_ENIGMA_Stras -->
    - utter_goodbye   <!-- predicted: action_listen -->
* goodbye: a bientôt
    - action_listen   <!-- predicted: utter_thanks -->


## greet and 2 faq no3 (/tmp/tmpvvzewwcn/708924ba52384104a6f4e4549c8ceed0_test_stories.md)
* faq: combien ça coûte ?
    - action_set_faq_slot
    - respond_faq
    - utter_one_more_question
* faq: Combien de temps est-ce que ça dure ?
    - action_set_faq_slot
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle   <!-- predicted: utter_thanks -->
* deny: non
    - utter_before_end   <!-- predicted: utter_question_on_ENIGMA_Stras -->
    - utter_goodbye   <!-- predicted: action_listen -->
* goodbye: a bientôt
    - action_listen   <!-- predicted: utter_thanks -->


## greet, 1 riddle, 1 faq (/tmp/tmpvvzewwcn/708924ba52384104a6f4e4549c8ceed0_test_stories.md)
* greet: coucou
    - utter_greet_and_propose_riddle   <!-- predicted: utter_greet -->
* affirm: wé
    - form_riddle
    - form{"name": "form_riddle"}
    - form{"name": null}
    - utter_propose_riddle
* deny: non
    - utter_question_on_ENIGMA_Stras
* affirm: oui
    - utter_question   <!-- predicted: utter_propose_riddle -->
* faq: faut-il prévoir à manger ?
    - action_set_faq_slot
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_thanks
    - utter_goodbye
* goodbye: a+
    - action_listen   <!-- predicted: action_default_fallback -->


## greet, 1 faq, 1 riddle (/tmp/tmpvvzewwcn/708924ba52384104a6f4e4549c8ceed0_test_stories.md)
* greet: coucou
    - utter_greet
* affirm: oui
    - utter_question   <!-- predicted: form_riddle -->
* faq: si la météo est mauvaise ?
    - action_set_faq_slot
    - respond_faq
    - utter_one_more_question
* deny: no
    - utter_propose_riddle   <!-- predicted: utter_thanks -->
* affirm: wé
    - form_riddle
    - form{"name": "form_riddle"}
    - form{"name": null}
    - utter_propose_riddle
* deny: non
    - utter_thanks   <!-- predicted: utter_question_on_ENIGMA_Stras -->
    - utter_goodbye
* goodbye: salut



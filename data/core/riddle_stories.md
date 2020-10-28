## enigmabot make a riddle
* ask_for_riddle OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## User accepted riddle without FAQ
> check_answer_about_riddle
* affirm OR ask_for_riddle OR inform_kind_of_riddle{"riddle_category": "logique"}
> to_riddle_1

## User accepted riddle without FAQ
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm OR ask_for_riddle OR inform_kind_of_riddle{"riddle_category": "logique"}
> to_riddle_2

## User accepted riddle after FAQ
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras


## User accepted riddle without FAQ - user ask to stop but then continue
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* stop OR no_more_riddle OR deny
  - utter_ask_leave_riddle_form
* deny
  - form_riddle
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ - user ask to stop but then continue
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* stop OR no_more_riddle OR deny
  - utter_ask_leave_riddle_form
* deny
  - form_riddle
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## User accepted riddle without FAQ - user ask to stop but then leave
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* stop OR no_more_riddle OR deny
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ - user ask to stop but then leave
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* stop OR no_more_riddle OR deny
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras


## User accepted riddle without FAQ - interruption with FAQ and stay
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* faq
  - respond_faq
  - utter_ask_leave_riddle_form
* deny
  - form_riddle
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ - interruption with FAQ and stay
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* faq
  - respond_faq
  - utter_ask_leave_riddle_form
* deny
  - form_riddle
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## User accepted riddle without FAQ - interruption with FAQ then leave
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* faq
  - respond_faq
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ - interruption with FAQ then leave
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* faq
  - respond_faq
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## User accepted riddle without FAQ - interruption with OOS and stay
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* out_of_scope
  - respond_out_of_scope
  - utter_ask_leave_riddle_form
* deny
  - form_riddle
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ - interruption with OOS and stay
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* out_of_scope
  - respond_out_of_scope
  - utter_ask_leave_riddle_form
* deny
  - form_riddle
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## User accepted riddle without FAQ - interruption with OOS then leave
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* out_of_scope
  - respond_out_of_scope
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ - interruption with OOS then leave
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* out_of_scope
  - respond_out_of_scope
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## User accepted riddle without FAQ - interruption with game presentation and stay
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* question_pitch
  - action_which_game
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"} OR meurtre_krutenau{"game": "Meurtre à la Krutenau"}
 - action_requested_game
* deny OR affirm
  - action_next_game
  - utter_ask_leave_riddle_form
* deny
  - form_riddle
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ - interruption with game presentation and stay
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* question_pitch
  - action_which_game
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"} OR meurtre_krutenau{"game": "Meurtre à la Krutenau"}
 - action_requested_game
* deny OR affirm
  - action_next_game
  - utter_ask_leave_riddle_form
* deny
  - form_riddle
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## User accepted riddle without FAQ - interruption with game presentation then leave
> to_riddle_1
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* question_pitch
  - action_which_game
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"} OR meurtre_krutenau{"game": "Meurtre à la Krutenau"}
 - action_requested_game
* deny OR affirm
  - action_next_game
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
> check_answer_about_riddle

## User accepted riddle after FAQ - interruption with game presentation then leave
> to_riddle_2
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* question_pitch
  - action_which_game
* societe_mysterieuse{"game": "Société Mystérieuse de Strasbourg"} OR meurtre_krutenau{"game": "Meurtre à la Krutenau"}
 - action_requested_game
* deny OR affirm
  - action_next_game
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - utter_ok
  - utter_an_other_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

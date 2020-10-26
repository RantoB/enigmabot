## enigmabot make a riddle
* ask_for_riddle OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## Bot proposed a riddle and user affirm without FAQ
> check_answer_about_riddle
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle

## Bot proposed a riddle and user affirm after FAQ
> check_answer_about_riddle_after_question_ENIGMA_Stras
* ask_for_riddle OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
  - form{"name": null}
  - utter_propose_riddle
> check_answer_about_riddle_after_question_ENIGMA_Stras

## Bot proposed a riddle and user affirm without FAQ - interruption with FAQ then leave
> check_answer_about_riddle
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
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

## Bot proposed a riddle and user affirm after FAQ - interruption with FAQ then leave
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
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

## Bot proposed a riddle and user affirm without FAQ - interruption with FAQ and stay
> check_answer_about_riddle
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* faq
  - respond_faq
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - form{"name": null}
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_riddle

## Bot proposed a riddle and user affirm after FAQ - interruption with FAQ and stay
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* faq
  - respond_faq
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - form{"name": null}
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_riddle_after_question_ENIGMA_Stras

## Bot proposed a riddle and user affirm without FAQ - interruption with OOS then leave
> check_answer_about_riddle
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
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

## Bot proposed a riddle and user affirm after FAQ - interruption with OOS then leave
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
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

## Bot proposed a riddle and user affirm without FAQ - interruption with OOS and stay
> check_answer_about_riddle
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* out_of_scope
  - respond_out_of_scope
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - form{"name": null}
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_riddle

## Bot proposed a riddle and user affirm after FAQ - interruption with OOS and stay
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
  - action_reset_riddle_slots
  - form_riddle
  - form{"name": "form_riddle"}
* out_of_scope
  - respond_out_of_scope
  - utter_ask_leave_riddle_form
* affirm
  - action_deactivate_form
  - form{"name": null}
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_riddle_after_question_ENIGMA_Stras

## Bot proposed a riddle and user affirm without FAQ - interruption with game presentation then leave
> check_answer_about_riddle
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
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

## Bot proposed a riddle and user affirm after FAQ - interruption with game presentation then leave
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
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

## Bot proposed a riddle and user affirm without FAQ - interruption with game presentation and stay
> check_answer_about_riddle
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
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
  - form{"name": null}
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_riddle

## Bot proposed a riddle and user affirm after FAQ - interruption with game presentation and stay
> check_answer_about_riddle_after_question_ENIGMA_Stras
* affirm OR inform_kind_of_riddle{"riddle_category": "logique"}
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
  - form{"name": null}
  - utter_ok
  - utter_question_on_ENIGMA_Stras
> check_answer_about_riddle_after_question_ENIGMA_Stras

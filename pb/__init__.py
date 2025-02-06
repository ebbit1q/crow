__all__ = [
    'admin_commands_pb2',
    'card_attributes_pb2',
    'color_pb2',
    'command_attach_card_pb2',
    'command_change_zone_properties_pb2',
    'command_concede_pb2',
    'command_create_arrow_pb2',
    'command_create_counter_pb2',
    'command_create_token_pb2',
    'command_deck_del_dir_pb2',
    'command_deck_del_pb2',
    'command_deck_download_pb2',
    'command_deck_list_pb2',
    'command_deck_new_dir_pb2',
    'command_deck_select_pb2',
    'command_deck_upload_pb2',
    'command_del_counter_pb2',
    'command_delete_arrow_pb2',
    'command_draw_cards_pb2',
    'command_dump_zone_pb2',
    'command_flip_card_pb2',
    'command_game_say_pb2',
    'command_inc_card_counter_pb2',
    'command_inc_counter_pb2',
    'command_kick_from_game_pb2',
    'command_leave_game_pb2',
    'command_move_card_pb2',
    'command_mulligan_pb2',
    'command_next_turn_pb2',
    'command_ready_start_pb2',
    'command_replay_delete_match_pb2',
    'command_replay_download_pb2',
    'command_replay_list_pb2',
    'command_replay_modify_match_pb2',
    'command_reveal_cards_pb2',
    'command_reverse_turn_pb2',
    'command_roll_die_pb2',
    'command_set_active_phase_pb2',
    'command_set_card_attr_pb2',
    'command_set_card_counter_pb2',
    'command_set_counter_pb2',
    'command_set_sideboard_lock_pb2',
    'command_set_sideboard_plan_pb2',
    'command_shuffle_pb2',
    'commands_pb2',
    'command_undo_draw_pb2',
    'context_concede_pb2',
    'context_connection_state_changed_pb2',
    'context_deck_select_pb2',
    'context_move_card_pb2',
    'context_mulligan_pb2',
    'context_ping_changed_pb2',
    'context_ready_start_pb2',
    'context_set_sideboard_lock_pb2',
    'context_undo_draw_pb2',
    'event_add_to_list_pb2',
    'event_attach_card_pb2',
    'event_change_zone_properties_pb2',
    'event_connection_closed_pb2',
    'event_create_arrow_pb2',
    'event_create_counter_pb2',
    'event_create_token_pb2',
    'event_del_counter_pb2',
    'event_delete_arrow_pb2',
    'event_destroy_card_pb2',
    'event_draw_cards_pb2',
    'event_dump_zone_pb2',
    'event_flip_card_pb2',
    'event_game_closed_pb2',
    'event_game_host_changed_pb2',
    'event_game_joined_pb2',
    'event_game_say_pb2',
    'event_game_state_changed_pb2',
    'event_join_pb2',
    'event_join_room_pb2',
    'event_kicked_pb2',
    'event_leave_pb2',
    'event_leave_room_pb2',
    'event_list_games_pb2',
    'event_list_rooms_pb2',
    'event_move_card_pb2',
    'event_notify_user_pb2',
    'event_player_properties_changed_pb2',
    'event_remove_from_list_pb2',
    'event_remove_messages_pb2',
    'event_replay_added_pb2',
    'event_reveal_cards_pb2',
    'event_reverse_turn_pb2',
    'event_roll_die_pb2',
    'event_room_say_pb2',
    'event_server_complete_list_pb2',
    'event_server_identification_pb2',
    'event_server_message_pb2',
    'event_server_shutdown_pb2',
    'event_set_active_phase_pb2',
    'event_set_active_player_pb2',
    'event_set_card_attr_pb2',
    'event_set_card_counter_pb2',
    'event_set_counter_pb2',
    'event_shuffle_pb2',
    'event_user_joined_pb2',
    'event_user_left_pb2',
    'event_user_message_pb2',
    'game_commands_pb2',
    'game_event_container_pb2',
    'game_event_context_pb2',
    'game_event_pb2',
    'game_replay_pb2',
    'isl_message_pb2',
    'moderator_commands_pb2',
    'move_card_to_zone_pb2',
    'response_activate_pb2',
    'response_adjust_mod_pb2',
    'response_ban_history_pb2',
    'response_deck_download_pb2',
    'response_deck_list_pb2',
    'response_deck_upload_pb2',
    'response_dump_zone_pb2',
    'response_forgotpasswordrequest_pb2',
    'response_get_admin_notes_pb2',
    'response_get_games_of_user_pb2',
    'response_get_user_info_pb2',
    'response_join_room_pb2',
    'response_list_users_pb2',
    'response_login_pb2',
    'response_password_salt_pb2',
    'response_pb2',
    'response_register_pb2',
    'response_replay_download_pb2',
    'response_replay_list_pb2',
    'response_viewlog_history_pb2',
    'response_warn_history_pb2',
    'response_warn_list_pb2',
    'room_commands_pb2',
    'room_event_pb2',
    'serverinfo_arrow_pb2',
    'serverinfo_ban_pb2',
    'serverinfo_cardcounter_pb2',
    'serverinfo_card_pb2',
    'serverinfo_chat_message_pb2',
    'serverinfo_counter_pb2',
    'serverinfo_deckstorage_pb2',
    'serverinfo_game_pb2',
    'serverinfo_gametype_pb2',
    'serverinfo_player_pb2',
    'serverinfo_playerping_pb2',
    'serverinfo_playerproperties_pb2',
    'serverinfo_replay_match_pb2',
    'serverinfo_replay_pb2',
    'serverinfo_room_pb2',
    'serverinfo_user_pb2',
    'serverinfo_warning_pb2',
    'serverinfo_zone_pb2',
    'server_message_pb2',
    'session_commands_pb2',
    'session_event_pb2'
]


def do_import():
    import sys
    import os
    import importlib
    this_dir = os.path.dirname(os.path.abspath(__file__))
    back = [*sys.path]
    sys.path.insert(0, this_dir)
    for name in __all__:
        globals()[name] = importlib.import_module(name)

    sys.path = back


do_import()

import msvcrt as m

# This could be one solution for a keypress    
while(True):
    key_press_bytes = m.getch()
    key_press = key_press_bytes.decode('utf-8')
    #print(key_press)

    if(key_press == 'p'):
        break
    else:
        check_action_for_key(key_press)


def check_action_for_key(key):
    dict_of_actions = {"a": a_sound,
    "b": b_sound, "c": c_sound, "d": d_sound, "e": e_sound, 
    "f": f_sound, "g": g_sound, "h": h_sound, "i": i_sound, 
    "j": j_sound, "k": k_sound, "l": l_sound, "m": m_sound, 
    "n": n_sound, "o": o_sound, "q": q_sound, 
    "r": r_sound, "s": s_sound, "t": t_sound, "u": u_sound, 
    "v": v_sound, "w": w_sound, "x": x_sound, "y": y_sound, 
    "z": z_sound}
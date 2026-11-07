def generate_hashtag(s):
    if s == "":
        return False
    else:
        s_list = s.split() 
        s_list.insert(0, "#")
        for n in range(len(s_list)):
            s_list[n] = s_list[n].capitalize()
        final_string = "".join(s_list)
        if len(final_string) > 140:
            return False
        return final_string

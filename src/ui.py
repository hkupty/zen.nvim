""" Zen ui.

This is a pretty straightforward ui framework for neovim.

This allows standardizations and quick handling of common ui elements
The idea of this framework is to provide common solutions without hassle.
"""


class EmptyPromptError(Exception):
    """ User aborted prompt. """
    pass


def prompt(nvim, label):
    nvim.call("inputsave")
    ret = nvim.call("input", "{} ".format(label))
    nvim.call("inputrestore")

    if not ret:
        raise EmptyPromptError(msg)

    return ret


def selection_window(nvim, **options):
    size = len(options["select_options"]) + 4

    if "header" in options:
        size += 1

    size = min(size, 15)

    nvim.command("botright {} spl | enew".format(size))
    buf_id = nvim.call("bufnr", "$")
    sw_buf = nvim.buffers[buf_id]

    if "header" in options:
        sw_buf[0] = options["header"]

    select_options = options["select_options"]

    [nvim.command(i) for i in [
        "map <buffer> {} {}".format(k, c) for k, _, c in select_options
    ]]


    text = ["Select an option below:", ""] + [
        "    ({}) {}".format(k, t) for k, t, _ in select_options
    ]

    sw_buf.append(text)


def build_window(nvim, **kwargs):
    orientation = kwargs.get('orientation', "topleft vertical split")
    cmds = [orientation, "enew"]

    if 'close' in kwargs:
        cmds.append('nmap <buffer> <silent> q :bd! %<CR>')

    if 'commands' in kwargs:
        cmds.extend(kwargs['commands'])

    try:
        nvim.command('|'.join(cmds))
    except:
        return None
    else:
        return nvim.funcs.bufnr('$')


def toggleable_buffer(nvim, buf_id, create_new_fn, **kwargs):
    orientation = kwargs.get('orientation', 'vertical split')
    win_nr = nvim.funcs.bufwinnr(buf_id)

    if win_nr == -1:
        if nvim.funcs.bufname(buf_id) == "":
            create_new_fn()
        else:
            nvim.command('{} | b {}'.format(orientation, buf_id))
    else:
        nvim.command('{} wincmd w | q | stopinsert'.format(win_nr))

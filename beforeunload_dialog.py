#Городецкий Тимофей
#12.11.2026
#14:44
#
def handle_dialog(dialog):
    assert dialog.type == 'beforeunload'
    dialog.dismiss()

page.on('dialog', handle_dialog)
page.close(run_before_unload=True)

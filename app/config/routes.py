
from system.core.router import routes

routes['default_controller'] = 'Notes'
routes['POST']['/add'] = 'Notes#add'
routes['POST']['/desc'] = 'Notes#description'
routes['GET']['/delete/<int:id>'] = 'Notes#delete'
routes['GET']['/partialindex'] = 'Notes#partialindex'

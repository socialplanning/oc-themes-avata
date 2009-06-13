from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from opencore.nui.main.view import GetStarted as GetStartedBase

class GetStarted(GetStartedBase):
    render = ViewPageTemplateFile('get-started.pt')

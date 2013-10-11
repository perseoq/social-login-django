SECURE_API_URL="https://api.loginradius.com/"
HEADERS={}
HEADERS['Accept'] = "application/json"

class LoginRadius():
        def __init__(self, API_Secret, Token):
                self.api_secret = API_Secret
                self.token = Token
                #We prefer to use requests with the updated urlib3.
                try:
                        import requests
                        self.library="requests"
                        self.requests = requests
                        self.urllib2 = False
                
                #However, we can use urllib if there is no requests.
                except:
                        import urllib
                        import urllib2
                        import json
                        self.library="urlib2"
                        self.urllib2 = urllib2
                        self.urllib = urllib
                        self.json = json
                        self.requests = False
                        
        #
        # Read Permissions
        #
        def loginradius_get_json(self, url, payload):
                if self.requests:
                        r = self.requests.get(url, params=payload, headers=HEADERS)
                        return r.json()
                else:
                        payload = self.urllib.urlencode(payload)
                        r = self.urllib2.Request(url + "?" + payload)
                        r.add_header('Accept', HEADERS['Accept'])
                        
                        try:
                                data = self.urllib2.urlopen(r)   
                        except self.urllib2.HTTPError, error:
                                return self.json.load(error)
                        return self.json.load(data)
                
        #Get access token                           
        def loginradius_get_accesstoken(self):
                payload = {'token':self.token,'secret':self.api_secret}
                url = SECURE_API_URL + "api/v2/access_token"
                return self.loginradius_get_json(url, payload)
        
        #Get User Profile data               
        def loginradius_get_userprofile(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/userprofile/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw User Profile Data
        def loginradius_get_userprofile_raw(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/userprofile/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Photos data using Album ID
        def loginradius_get_photo(self, access_token, albumid = None):
                if albumid is  None:
                        albumid = ''
                payload ={'access_token':access_token,'albumid':albumid}
                url =SECURE_API_URL + "api/v2/photo/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Photos data using Album ID
        def loginradius_get_photo_raw(self, access_token, albumid = None):
                if albumid is  None:
                        albumid = ''
                payload ={'access_token':access_token,'albumid':albumid}
                url =SECURE_API_URL + "api/v2/photo/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Check in data
        def loginradius_get_checkin(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/checkin/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Check in data 
        def loginradius_get_checkin_raw(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/checkin/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Album data
        def loginradius_get_album(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/album/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Album data
        def loginradius_get_album_raw(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/album/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Audio Data
        def loginradius_get_audio(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/audio/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Audio Data
        def loginradius_get_audio_raw(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/audio/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Video Data
        def loginradius_get_video(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/video/"
                return self.loginradius_get_json(url, payload)
        #Get Raw Video Data
        def loginradius_get_video_raw(self, access_token):
                payload ={'access_token':access_token}
                url =SECURE_API_URL + "api/v2/video/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Contacts Data          
        def loginradius_get_contacts(self, access_token, next_cursor = None):
                if next_cursor is  None:
                        next_cursor = ''
                payload = {'access_token':access_token,'nextcursor':next_cursor}
                url =SECURE_API_URL + "api/v2/contact/"
                return self.loginradius_get_json(url, payload)
        #Get Raw Contacts Data
        def loginradius_get_contacts_raw(self, access_token, next_cursor = None):
                if next_cursor is  None:
                        next_cursor = ''
                payload = {'access_token':access_token,'nextcursor':next_cursor}
                url =SECURE_API_URL + "api/v2/contact/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Status Data        
        def loginradius_get_status(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/status/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Status Data
        def loginradius_get_status_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/status/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Group Data    
        def loginradius_get_group(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/group/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Group Data
        def loginradius_get_group_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/group/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Post Data
        def loginradius_get_post(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/post/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Post Data
        def loginradius_get_post_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/post/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Event Data               
        def loginradius_get_event(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/event/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Event Data
        def loginradius_get_event_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/event/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Mention Data
        def loginradius_get_mention(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/mention/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Mention Data
        def loginradius_get_mention_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/mention/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Company Data
        def loginradius_get_company(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/company/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Company Data 
        def loginradius_get_company_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/company/raw/"
                return self.loginradius_get_json(url, payload)
            
        #Get Following Data  
        def loginradius_get_following(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/following/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Following Data  
        def loginradius_get_following_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/following/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Activity Data  
        def loginradius_get_activity(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/activity/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Activity Data  
        def loginradius_get_activity_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/activity/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Page Data  
        def loginradius_get_page(self, access_token, pagename):
                payload ={'access_token':access_token,'pagename':pagename}
                url = SECURE_API_URL + "api/v2/page/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Page Data  
        def loginradius_get_page_raw(self, access_token, pagename):
                payload ={'access_token':access_token,'pagename':pagename}
                url = SECURE_API_URL + "api/v2/page/raw/"
                return self.loginradius_get_json(url, payload)
        
        #Get Likes Data
        def loginradius_get_like(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/like/"
                return self.loginradius_get_json(url, payload)
        
        #Get Raw Likes Data  
        def loginradius_get_like_raw(self, access_token):
                payload ={'access_token':access_token}
                url = SECURE_API_URL + "api/v2/like/raw/"
                return self.loginradius_get_json(url, payload)
                
        #
        #Write Permissions
        #
        def loginradius_post_data(self, url, payload):
                if self.requests:
                        import json
                        data = json.dumps(payload)
                        r = self.requests.post(url + "?" + data, params=payload, headers=HEADERS)
                        return r.json()
                else:
                        payload = self.urllib.urlencode(payload)
                        r = self.urllib2.Request(url + "?" + payload, '', {'Content-Type': 'application/json'})
                        r.add_header('Accept', HEADERS['Accept'])
                        try:
                                data = self.urllib2.urlopen(r)
                        except self.urllib2.HTTPError, error:
                                return self.json.load(error)
                        return self.json.load(data)
                        
        #Update the Status        
        def loginradius_status_update(self, access_token, status, title = None, url= None, imageurl= None, caption=None, description=None):
                if title is  None:
                        title = ''
                if url is  None:
                        url = ''
                if imageurl is  None:
                        imageurl = ''
                if caption is  None:
                        caption = ''
                if description is  None:
                        description = ''
                payload = {'access_token':access_token,'status':status,'title':title,'url':url,'imageurl':imageurl,'caption':caption,'description':description}
                url = SECURE_API_URL + "api/v2/status/"
                return self.loginradius_post_data(url, payload)
        
        #Update the Direct Message
        def loginradius_direct_message(self, access_token, to, subject, message):
                payload = {'access_token':access_token,'to': to, 'subject': subject, 'message':message}
                url = SECURE_API_URL + "api/v2/message/"
                return self.loginradius_post_data(url, payload)
                        
                        
                        


                        
                

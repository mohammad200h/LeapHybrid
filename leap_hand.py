# PyMJCF
from dm_control import mjcf


class LeapHand(object):
  def __init__(self):

    # palm
    palm = mjcf.from_path("./palm.xml")
    
    # attach 3 fingers to palm sites
    for finger in ["FF","MF","RF"]:
      site = palm.find('site',finger)
      finger_model = mjcf.from_path("./finger.xml")
      site.attach(finger_model)

    # attach thumb to palm site 
    site = palm.find('site',"TH")
    thumb_model = mjcf.from_path("./thumb.xml")
    site.attach(thumb_model)

    self.model = palm




hand = LeapHand()

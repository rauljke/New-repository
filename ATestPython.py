def set_cam_cfg(self, cam_cfg):
        """
        In case we need to reconfigure for a different cam cfg
        :param cam_cfg: the new cam_cfg
        :return: None
        """
        # close the current connections
        self.mcu.disconnect()
        self.isp.disconnect()
        self.mcu = None
        self.isp = None

        # set new config
        self.cam_cfg = cam_cfg
        self.cam_defaults = self.utils.defaults.get_defaults_cam(cam_cfg.get('model'))
        self.mcu = SerialMCU(self.utils, self.cam_cfg)
        self.isp = SerialISP(self.utils, self.cam_cfg)

       def connect_uart(self):
        self.mcu.connect()
        self.isp.connect()
        self.connected = True
     
        

rest = {'hostname': '172.31.52.141', 'platform': 'Amazon Linux (64 bit)', 'lastModified': 1507111935833, 'instanceId': 'i-0f8b27c5f614d3ad3', 'lastIpUsed': '', 'created': 1498218514097, 'lastUpdateAttempt': None, 'displayname': 'LRV-PRD-EC2-RNGINX-0002', 'id': 350, 'description': '', 'hostGroupId': 0, 'agentReportedVersion': 'Trend Micro Deep Security Agent (9.6.2.8140)', 'externalId': '', 'policy': None}
soap = {"ID": 350, "description": None, "name": "172.31.52.141", "displayName": "LRV-PRD-EC2-RNGINX-0002", "external": True, "externalID": None, "hostGroupID": 1, "hostType": "STANDARD", "platform": "Amazon Linux (64 bit) (4.9.27-14.31.amzn1.x86_64)", "securityProfileID": 35, "antiMalwareClassicPatternVersion": "N/A", "antiMalwareEngineVersion": "N/A", "antiMalwareIntelliTrapExceptionVersion": "N/A", "antiMalwareIntelliTrapVersion": "N/A", "antiMalwareSmartScanPatternVersion": "N/A", "antiMalwareSpywarePatternVersion": "N/A", "cloudObjectImageId": "ami-95eaf1f3", "cloudObjectInstanceId": "i-0f8b27c5f614d3ad3", "cloudObjectInternalUniqueId": "i-0f8b27c5f614d3ad3", "cloudObjectSecurityGroupIds": "LRV_PRD_SG_ELK-SW-01, LRV-PRD-SG-RNGINX-01", "cloudObjectType": "AMAZON_VM", "componentKlasses": {"item": []}, "componentNames": {"item": []}, "componentTypes": {"item": []}, "componentVersions": {"item": []}, "hostGroupName": "Computers > LayerV PROD Account - EU (Ireland)", "hostInterfaces": {"item": [{"ID": None, "description": None, "name": "eth0", "displayName": None, "external": False, "externalID": None, "hostGroupID": None, "hostType": None, "platform": None, "securityProfileID": None, "dhcp": False, "hostBridgeId": None, "interfaceTypeId": None, "mac": "02:A7:68:8F:E8:12", "notAvailable": False, "virtualDeviceKey": None}]}, "hostLight": "GREEN", "lastAnitMalwareScheduledScan": None, "lastAntiMalwareEvent": None, "lastAntiMalwareManualScan": None, "lastDpiEvent": "2017-10-09 11:00:24.467000+00:00", "lastFirewallEvent": "2017-10-02 14:21:53.437000+00:00", "lastIPUsed": "172.31.68.6", "lastIntegrityMonitoringEvent": None, "lastLogInspectionEvent": None, "lastWebReputationEvent": None, "light": 0, "locked": False, "overallAntiMalwareStatus": "Anti-Malware: Off, not installed, no configuration", "overallDpiStatus": "Intrusion Prevention: On, Detect, 87 rules", "overallFirewallStatus": "Firewall: Off, installed, no rules", "overallIntegrityMonitoringStatus": "Integrity Monitoring: On, 9 rules", "overallLastRecommendationScan": None, "overallLastSuccessfulCommunication": "2017-10-09 11:14:32.203000+00:00", "overallLastSuccessfulUpdate": "2017-10-04 10:12:48.700000+00:00", "overallLastUpdateRequired": "2017-10-04 10:12:15.833000+00:00", "overallLogInspectionStatus": "Log Inspection: Off, not installed, no rules", "overallStatus": "Managed (Online)", "overallVersion": "9.6.2.8140", "overallWebReputationStatus": "Web Reputation: Off, not installed", "securityProfileName": "LRV-PRD-NGINX", "virtualName": None, "virtualUuid": None}


def join_lists(master_list, slave_list, keys_list):
    slave_dict = dict((item['id'], item) for item in slave_list)
    arr = list()
    for item in master_list:
        augmentable = item
        for k in keys_list:
            if item['id'] in slave_dict:
                augmentable[k] = slave_dict[item['id']][k]
        arr.append(augmentable)
    return arr


def list_analyser(obj_a, obj_b):
    def key_by_value(obj, search_value):
        for k, v in obj.items():
            if v == search_value:
                return k

    common = list()
    items = obj_a.copy()
    for key, value in items.items():
        if key in obj_b.keys():
            obj_a.pop(key)
            obj_b.pop(key)
        if value and value in obj_b.values():
            key_b = key_by_value(obj_b, value)
            common.append({"{} => {}".format(key, key_b): value})
            obj_a.pop(key)
            obj_b.pop(key_b)

    return {'different_key_name': common, 'first_list_has_extra': obj_a, 'secont_list_has_extra': obj_b}

result = list_analyser(rest, soap)
print('***different_key_name***', result['different_key_name'])
print('***first_list_has_extra***', result['first_list_has_extra'])
print('***secont_list_has_extra***', result['secont_list_has_extra'])
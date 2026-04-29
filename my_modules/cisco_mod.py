from ansible.module_utils.basic import AnsibleModule



def switch():
    module_args=dict(
        interface=dict(type=str, required=True)
        vlan=dict(type=int, required=True,default=1)
    )
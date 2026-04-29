from ansible.module_utils.basic import AnsibleModule



def saribeg():
    module_args = dict(
        name=dict(type=str, required=True),
        new=dict(type=bool, required=False, default=False) 
    )
    
    result = dict(
        changed=False,
        original_message= '',
        message=''
    )
    
    module = AnsibleModule(
        argument_spec = module_args,
        supports_check_mode = True
    )
    
    if module.check_mode:
            return result
    
    
    result['original_message'] = module.params['name']
    result['message'] = 'goodbye'
    
    
    if module.params['new']:
        result['changed'] = True
    
    
    if module.params['name'] == 'fail me':
        module.fail_json(msg='the required parameter is wrong', **result)
    
    
    module.exit_json()
    
def main():
    saribeg()
    
if __name__ == "__main__":
    main()
    
    
    
/** @odoo-module **/

import { registerPatch } from '@mail/model/model_core';
import { attr, one } from '@mail/model/model_field';
import { clear } from '@mail/model/model_field_command';
import { sprintf } from '@web/core/utils/strings';
import rpc from 'web.rpc';
    var core = require('web.core');
    var QWeb = core.qweb;
    var Dialog = require('web.Dialog');

registerPatch({
    /** This function was used to overall confirm the
    deletion of attachments and handle user permissions **/
    name: 'AttachmentDeleteConfirmView',
    recordMethods: {
        async onClickOk() {
         const chatter = this.chatter;
         var self = this;
         /** This RPC used to  "get_user"  take current
         login user of the "ir.attachment" model. **/
         await rpc.query({
            model:'ir.attachment',
            method:'get_user',
            args:[[self.attachment.id]],
         }).then(function([user, result]){
         console.log(user)
         if (user){
            self.attachment.remove();
         }
         if(result){
             Dialog.alert(
                        this,
                              "This request already created.",
                              {
                           onForceClose: function(){
                           },
                        });
         }else{
            /**This RPC used to user can allow all models **/
            rpc.query({
            model:'ir.attachment',
            method :'all_models',
            args:[[]],
         }).then(function(result){
             if (result){
                  self.env.services.orm.unlink('ir.attachment', [self.attachment.id])
                  self.dialogOwner.delete();
                   Dialog.alert(
                        this,
                              "Your Approval Request was successfully sent to the approver.Once the approver accepts the request, the attachment will be automatically removed.",
                              {
                           onForceClose: function(){
                           },
                        });
             }else{
                 rpc.query({
                 model:'ir.attachment',
                 method:'models',
                 args:[[self.attachment.id]],
             }).then(function(result){
                 if (result == true){
                     self.env.services.orm.unlink('ir.attachment', [self.attachment.id])
                     self.dialogOwner.delete();
                     Dialog.alert(
                        this,
                              "Your Approval Request was successfully sent to the approver.Once the approver accepts the request, the attachment will be automatically removed.",
                              {
                           onForceClose: function(){
                           },
                        });
                 }else{
                     Dialog.alert(
                        this,
                        "You Have No rights to delete this attachment Please Contact Your ADMINISTRATOR ",
                        {
                           onForceClose: function(){
                           },
                        });
                }
             })
            }
         })
        }
        })
        if (chatter && chatter.exists() && chatter.shouldReloadParentFromFileChanged) {
            chatter.reloadParentView();
        }
    },
    },
    });
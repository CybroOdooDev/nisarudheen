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
    name: 'AttachmentDeleteConfirmView',
    recordMethods: {
        async onClickOk() {

         const chatter = this.chatter;
         var self = this;
         await rpc.query({
            model:'ir.attachment',
            method:'get_user',
            args:[[]],
         }).then(function(result){
         if (result){
            self.attachment.remove();
         }else{
             console.log(self.attachment.id)
             rpc.query({
                model:'ir.attachment',
                method:'models',
                args:[[self.attachment.id]],
              })
              self.env.services.orm.unlink('ir.attachment', [self.attachment.id])
              self.dialogOwner.delete();
        }
        })
        if (chatter && chatter.exists() && chatter.shouldReloadParentFromFileChanged) {
            chatter.reloadParentView();
        }
    },
    },
    });
# -*- coding: utf-8 -*-
from odoo import api
from odoo import models, fields
from odoo import tools
from odoo.tools.translate import _


class Gametype(models.Model):
    _name = "thnolg.gametype"
    _description = _("Gametype")

    name = fields.Char(required=True, string="Name")
    game_gametypes = fields.One2many("thnolg.gamegametype", inverse_name="gametype", string="Gametypes")


class Game(models.Model):
    _name = "thnolg.game"
    _description = _("Game")

    tag = fields.Char(required=True, string="Tag")
    friendly_name = fields.Char(string="Friendly Name")
    icon = fields.Binary(attachment=True, string="Icon")
    game_gametypes = fields.One2many("thnolg.gamegametype", inverse_name="game", string="Gametypes")

    @api.multi
    def name_get(self):
        result = []
        for record in self:
            if record.friendly_name is not None and len(record.friendly_name) > 0:
                result.append((record.id, record.friendly_name))
            else:
                result.append((record.id, record.tag))
        return result

    @api.onchange("icon")
    def _resize_icon(self):
        self.icon = tools.image_resize_image(self.icon, size=(48, 48))

    class GameGametype(models.Model):
        _name = "thnolg.gamegametype"

        game = fields.Many2one("thnolg.game", string="Game")
        gametype = fields.Many2one("thnolg.gametype", string="Gametype")
        tag = fields.Char(required=True, string="Tag")

    class OlgServer(models.Model):
        _name = "thnolg.olgserver"
        _description = _("Server")

        enabled = fields.Boolean(required=True, default=True, string="Enabled")
        tag = fields.Char(required=True, string="Tag")
        friendly_name = fields.Char(string="Friendly Name")
        name = fields.Char(string="Name")
        address = fields.Char(required=True, string="Address")
        port = fields.Integer(required=True, string="Port")
        game = fields.Many2one("thnolg.game", string="Game")
        rcon_password = fields.Char(string="RCON Password")
        enable_adv = fields.Boolean(required=True, default=True, string="Enable Adv")

        @api.multi
        def name_get(self):
            result = []
            for record in self:
                if record.friendly_name is not None and len(record.friendly_name) > 0:
                    result.append((record.id, record.friendly_name))
                elif record.name is not None and len(record.name) > 0:
                    result.append((record.id, record.name))
                else:
                    result.append((record.id, record.tag))
            return result

    class OlgMap(models.Model):
        _name = "thnolg.olgmap"
        _description = _("Map")

        tag = fields.Char(required=True, string="Tag")
        friendly_name = fields.Char(string="Friendly Name")
        game = fields.Many2one("thnolg.game", string="Game")
        gametypes = fields.Many2many("thnolg.gametype", string="Gametypes")
        servers = fields.Many2many("thnolg.olgserver", string="Servers")

        @api.multi
        def name_get(self):
            result = []
            for record in self:
                if record.friendly_name is not None and len(record.friendly_name) > 0:
                    result.append((record.id, record.friendly_name))
                else:
                    result.append((record.id, record.tag))
            return result

    class Player(models.Model):
        _name = "thnolg.player"
        _description = _("Player")

        name = fields.Char(string="Name")
        guid = fields.Char(string="GUID")
        user = fields.Many2many("res.users")
        game = fields.Many2one("thnolg.game", string="Game")
        servers = fields.Many2one("thnolg.olgserver", string="Servers")

    class Adv(models.Model):
        _name = "thnolg.adv"
        _description = _("Advertise")
        _rec_name = "message"

        message = fields.Text(required=True, string="Message")
        priority = fields.Integer(required=True, default=1, string="Priority")
        weight = fields.Integer(required=True, default=1, string="Weight")
        enabled = fields.Boolean(required=True, default=True, string="Enabled")

    class AdvServer(models.Model):
        _name = "thnolg.advserver"

        adv = fields.Many2one("thnolg.adv", string="Advertisement")
        server = fields.Many2one("thnolg.olgserver", string="Server")
        enabled = fields.Boolean(required=True, default=True, string="Enabled")

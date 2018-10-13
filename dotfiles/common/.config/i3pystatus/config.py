from i3pystatus import Status
from i3pystatus.weather import weathercom
from i3pystatus.updates import pacman, cower
from i3pystatus.mail import imap


status = Status(
    logfile='/home/sergei/var/i3pystatus.log',
    logformat='%(asctime)s %(levelname)s:',
    keep_alive=True,
    )


status.register(
    'weather',
    format='{current_temp}{temp_unit}',
    colorize=False,
    backend=weathercom.Weathercom(
        location_code='RSVR1844:1:RS',
        units='metric',
        ),
    hints = {"separator": False, "separator_block_width": 15},
    )


# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %d %b. %H:%M",
    #"%a %-d %b %X KW%V",)
    hints = {"separator": False, "separator_block_width": 15},
    )


# The battery monitor has many formatting options, see README for details

# This would look like this, when discharging (or charging)
# ↓14.22W 56.15% [77.81%] 2h:41m
# And like this if full:
# =14.22W 100.0% [91.21%]
#
# This would also display a desktop notification (via D-Bus) if the percentage
# goes below 5 percent while discharging. The block will also color RED.
# If you don't have a desktop notification demon yet, take a look at dunst:
#   http://www.knopwob.org/dunst/
status.register("battery",
    format="{status}.{percentage:.0f}",
    alert=False,
    no_text_full=True,
#    alert_percentage=5,
    color='#ffffff',
    charging_color='#ffffff',
    critical_color='#ffffff',
    status={
        "DIS": "",
        "CHR": "",
        "FULL": "=",
        },
    hints = {"separator": False, "separator_block_width": 15},
    )

#
#status.register("scratchpad",
#    format = "{number}",
#    always_show=False,
#    color_urgent='#ffffff',
#    hints = {"separator": False, "separator_block_width": 15},
#    )


status.register("mail",
        	format = '{unread}',
                backends=[imap.IMAP(
                    host="imap.gmail.com", username="ser.zhdanov@gmail.com",
                    password="shukmxucgicjchii")],
                color_unread='#ffffff',
                hints = {"separator": False, "separator_block_width": 15},
                )


status.register("updates",
                format = "{count}",
                format_working = "",
                backends = [pacman.Pacman(), cower.Cower()],
                color='#ffffff',
                interval=600,
                hints = {"separator": False, "separator_block_width": 15},
                )


#status.register("pomodoro",
#        format="{time}",
#        pomodoro_duration=20,
#        break_duration=10,
#        sound="~/Dropbox/sound.ogg",
#        )


status.run()

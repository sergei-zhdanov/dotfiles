from i3pystatus import Status
#from i3pystatus.weather import weathercom
from i3pystatus.updates import pacman, cower
from i3pystatus.mail import imap


status = Status(
    logfile='/home/sergei/var/i3pystatus.log',
    logformat='%(asctime)s %(levelname)s:',
    keep_alive=True,
    )


#status.register("weather",
#    format='{current_temp}{temp_unit}[ {update_error}]',
#    colorize=False,
#    interval=900,
#    backend=weathercom.Weathercom(
#        location_code='RSVR1844:1:RS',
#        units='metric',
#        update_error='шайтан!',
#        ),
#    hints = {"separator": False, "separator_block_width": 15},
#    )


status.register("shell",
    command='shaman -l voronezh -m -f %t\°C',
    interval=1800,
#    ignore_empty_stdout=True,
    error_color='#ffffff',
    hints = {"separator": False, "separator_block_width": 15},
    )

# Displays clock like this:
# Tue 30 Jul 11:59:46 PM KW31
#                          ^-- calendar week
status.register("clock",
    format="%a %-d %b. %H:%M",
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


#status.register("scratchpad",
#    format = "{number}",
#    always_show=False,
#    color_urgent='#ffffff',
#    hints = {"separator": False, "separator_block_width": 15},
#    )


#status.register("mail",
#        	format = '{unread}',
#        	format_plural = '{unread}',
#                backends=[imap.IMAP(
#                    host="imap.gmail.com", ssl=True, username="ser.zhdanov@gmail.com",
#                    password="shukmxucgicjchii")],
#                color_unread='#ffffff',
#                interval=900,
#                hints = {"separator": False, "separator_block_width": 15},
#                )
#

status.register("shell",
    format = '{output}',
    command='curl -u "ser.zhdanov@gmail.com":"shukmxucgicjchii" --silent "https://mail.google.com/mail/feed/atom" |  grep -oPm1 "(?<=<title>)[^<]+" | sed "1d" | wc -l',
    interval=900,
#    ignore_empty_stdout=True,
    error_color='#ffffff',
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


status.register("pomodoro",
        sound="/home/sergei/Dropbox/bell.wav",
#        format="[{time}]",
        format="{time}",
        format_break="{time}",
        pomodoro_duration=900,
        break_duration=300,
        long_break_duration=300,
        hints = {"separator": False, "separator_block_width": 15},
        )


status.run()

#!/bin/bash

state=$(fcitx5-remote)
if [ "$state" = "2" ]; then
    echo "🌸 JP"
elif [ "$state" = "1" ]; then
    echo "🅰️ EN"
else
    echo "⚠️ --"
fi

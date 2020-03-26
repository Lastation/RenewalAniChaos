Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      MoveUnit(All, "80 + 1n Tank", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      KillUnit("Protoss Observer", CurrentPlayer);
      ModifyUnitShields(All, " * Samir Duran", CurrentPlayer, "Anywhere", 1);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Samir Duran", CurrentPlayer, "Anywhere", Move, "14.Yashiro_Bozo");
   },
}

for i = 0, 7, 1 do

radius = 0 / 4 * math.pi;

d = 60 + i * 60;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      CreateUnit(4, "80 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "80 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      RemoveUnitAt(All, "80 + 1n Tank", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 7, 1 do

interval = 60 + i * 60;

d = 480;

x = d - interval;
y = interval;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      CreateUnit(4, "60 + 3n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "60 + 3n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      RemoveUnitAt(All, "60 + 3n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

interval = 60;

x = - interval * 8;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

x = 0;
y = - interval * 8;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}


x = interval * 8;
y = 0;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}


x = 0;
y = interval * 8;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(8, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, -interval);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillLoop3");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force1},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(3600);
      GiveUnits(All, "40 + 1n Wraith", CurrentPlayer, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Wraith", P7, "Anywhere", P12);
      Wait(900);
      GiveUnits(All, "40 + 1n Wraith", P12, "Anywhere", CurrentPlayer);
      SetDeaths(AllPlayers, SetTo, 14001, " `SkillText_Uiltimate");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : S
   players = {Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(3800);
      GiveUnits(All, "40 + 1n Wraith", CurrentPlayer, "Anywhere", P8);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Wraith", P8, "Anywhere", P12);
      Wait(900);
      GiveUnits(All, "40 + 1n Wraith", P12, "Anywhere", CurrentPlayer);
      SetDeaths(AllPlayers, SetTo, 14001, " `SkillText_Uiltimate");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}


for i = 0, 7, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Wraith", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "40 + 1n Marine", "[Skill]Unit_Wait_5", CurrentPlayer);
      CreateUnit(1, "50 + 1n Tank", "[Skill]Unit_Wait_6", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(1, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Wraith", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "40 + 1n Goliath", "[Skill]Unit_Wait_7", CurrentPlayer);
      CreateUnit(1, "40 + 1n Firebat", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", "40 + 1n Wraith", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      MoveUnit(1, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 16, " `SkillLoop2");
      Bring(CurrentPlayer, AtLeast, 1, "40 + 1n Wraith", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(All, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      RemoveUnitAt(All, "40 + 1n Marine", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      RemoveUnitAt(All, "50 + 1n Tank", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Firebat", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Goliath", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Order("40 + 1n Firebat", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop2");
      Bring(CurrentPlayer, Exactly, 0, "40 + 1n Wraith", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "40 + 1n Marine", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(All, "40 + 1n Firebat", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(All, "40 + 1n Goliath", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      RemoveUnitAt(All, "40 + 1n Marine", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      RemoveUnitAt(All, "50 + 1n Tank", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Firebat", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      RemoveUnitAt(All, "40 + 1n Goliath", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      Order("40 + 1n Marine", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Order("40 + 1n Firebat", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Order("40 + 1n Goliath", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(2000);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

interval = 75;

for i = 0, 6, 1 do

x = -interval * 3;
y = interval * 3 - interval * i;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

interval = 75;

for i = 0, 6, 1 do

x = -interval * 3;
y = interval * 3 - interval * i;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(0);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

interval = 75;

for i = 0, 6, 1 do

x = -interval * 3;
y = interval * 3 - interval * i;

x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(7, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("130 + 1n Norad", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(700);
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(900);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "80 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 3n Siege", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Marine", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Firebat", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Goliath", "Anywhere", CurrentPlayer);
      SetSwitch("UiltimateSwitch", Clear);
      Wait(500);
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}

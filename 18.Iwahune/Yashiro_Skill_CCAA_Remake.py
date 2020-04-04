Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
   },
   actions = {
      Comment("Skill : Ulitmate");
      PreserveTrigger();
      KillUnit("Protoss Observer", CurrentPlayer);
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro_Bozo", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Samir Duran", CurrentPlayer, "Anywhere", Move, "14.Yashiro_Bozo");
   },
}



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}

for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 50 + 50 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 50 + 50 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "40 + 1n Wraith", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Scantid (Desert)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Scantid (Desert)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      KillUnitAt(All, "Scantid (Desert)", "Anywhere", CurrentPlayer);
      Wait(0);
      RemoveUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 3, 1 do

radius = i / 8 * math.pi;

d = 170;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Tank", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(All, "50 + 1n Tank", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("50 + 1n Tank", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

for i = 0, 3, 1 do

radius = i / 8 * math.pi;

d = 170;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i + 4, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(200);
      SetDeaths(AllPlayers, SetTo, 2003, " `SkillText3");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

radius = 0 / 4 * math.pi;

d = 50 + i * 50;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


for i = 0, 3, 1 do

radius = 1 / 4 * math.pi;

d = 50 + i * 50;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "Protoss Dark Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(4, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "14.Yashiro");
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}

for i = 0, 7, 1 do

radius = i / 8 * math.pi;

d = 120;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(4, "130 + 1n Norad", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, x, y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -x, -y);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, -y, x);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      LMove(163, y, -x);
      MoveUnit(1, "130 + 1n Norad", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      KillUnitAt(All, "130 + 1n Norad", "Anywhere", CurrentPlayer);
      Wait(0);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
   },
}
end

interval = 75;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      CreateUnit(9, "50 + 1n Battlecruiser", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("14.Yashiro", " * Samir Duran", CurrentPlayer, "Anywhere");
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, -interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, 0, -interval);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      LMove(163, interval, 0);
      MoveUnit(1, "50 + 1n Battlecruiser", CurrentPlayer, "[Skill]Unit_Wait_ALL", "14.Yashiro");
      Order("50 + 1n Battlecruiser", CurrentPlayer, "Anywhere", Attack, "Anywhere");
      Wait(350);
      KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", CurrentPlayer);
      Wait(1500);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Samir Duran");
      Bring(CurrentPlayer, AtLeast, 1, " * Samir Duran", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 210, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Combo");
      PreserveTrigger();
      KillUnitAt(All, "50 + 1n Tank", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      Wait(500);
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}
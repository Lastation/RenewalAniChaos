Trigger { -- Skill : Unique
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(200);
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(200);
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(200);
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(200);
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      Wait(200);
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      CreateUnit(1, "80 + 1n Tom Kazansky", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21. Magellan", " * Probe", CurrentPlayer, "Anywhere");
      MoveUnit(1, "80 + 1n Tom Kazansky", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21. Magellan");
      SetSwitch("Unique - Magellan", Set);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 8, " `UniqueSkill");
      SetDeaths(CurrentPlayer, SetTo, 360, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 12, " `SkillWait");
      PreserveTrigger();
   },
}

Trigger { -- Skill : Unique
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, AtLeast, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Unique");
      SetDeaths(CurrentPlayer, Subtract, 1, " `SkillLoop4");
      PreserveTrigger();
   },
}


Trigger { -- Skill : Unique
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Unique");
      KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `UniqueSkill");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, "80 + 1n Tom Kazansky");
      SetSwitch("Unique - Magellan", Clear);
      SetDeaths(CurrentPlayer, SetTo, 1440, " `UniqueCoolTime");
      PreserveTrigger();
   },
}


Trigger { -- Skill : Unique
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Deaths(CurrentPlayer, AtLeast, 1, "80 + 1n Tom Kazansky");
   },
   actions = {
      Comment("Skill : Unique");
      SetDeaths(CurrentPlayer, SetTo, 0, " `UniqueSkill");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
      SetDeaths(CurrentPlayer, SetTo, 0, "80 + 1n Tom Kazansky");
      SetSwitch("Unique - Magellan", Clear);
      SetDeaths(CurrentPlayer, SetTo, 1440, " `UniqueCoolTime");
      PreserveTrigger();
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Cleared);
      Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      MoveLocation("21.Magellan_Bozo2", " * Probe", CurrentPlayer, "Anywhere");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Bring(CurrentPlayer, AtLeast, 1, "80 + 1n Tom Kazansky", "Anywhere");
      Switch("Unique - Magellan", Set);
      Bring(CurrentPlayer, Exactly, 0, "80 + 1n Tom Kazansky", "21.Magellan_Bozo2");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      MoveUnit(All, "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere", "21.Magellan_Bozo2");
   },
}


for i = 0, 1, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 4 * i + 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
   },
}

end


for i = 0, 3, 1 do

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `UniqueSkill");
      Deaths(CurrentPlayer, AtLeast, 101, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 199, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      KillUnitAt(All, "40 + 1n Wraith", "Anywhere", CurrentPlayer);
   },
}

end

x = 100;
y = 100;

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 8, " `UniqueSkill");
      Deaths(CurrentPlayer, AtLeast, 101, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 199, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 6, " `UniqueSkill");
      Deaths(CurrentPlayer, AtLeast, 101, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 199, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, -y, x);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, y, -x);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 4, " `UniqueSkill");
      Deaths(CurrentPlayer, AtLeast, 101, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 199, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, x, 0);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, -x, 0);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 2, " `UniqueSkill");
      Deaths(CurrentPlayer, AtLeast, 101, " `SkillStep");
      Deaths(CurrentPlayer, AtMost, 199, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(2, "40 + 1n Wraith", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, 0, y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, 0, -y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Wraith", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      Order("40 + 1n Wraith", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
   },
}

for i = 0, 7, 1 do

radius = i / 8 * math.pi;

d = 50;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, i + 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      RemoveUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      CreateUnit(2, "Protoss Dark Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, x, y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, -x, -y);
      MoveUnit(1, "Protoss Dark Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      KillUnitAt(All, "Protoss Dark Archon", "Anywhere", CurrentPlayer);
   },
}

end

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
      Bring(P1, AtLeast, 1, "Any unit", "21.Magellan_Bozo");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(P1, SetTo, 1, " `SystemDebuff_Stun");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
      Bring(P2, AtLeast, 1, "Any unit", "21.Magellan_Bozo");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(P2, SetTo, 1, " `SystemDebuff_Stun");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
      Bring(P3, AtLeast, 1, "Any unit", "21.Magellan_Bozo");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(P3, SetTo, 1, " `SystemDebuff_Stun");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
      Bring(P4, AtLeast, 1, "Any unit", "21.Magellan_Bozo");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(P4, SetTo, 1, " `SystemDebuff_Stun");
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
      Bring(P5, AtLeast, 1, "Any unit", "21.Magellan_Bozo");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(P5, SetTo, 1, " `SystemDebuff_Stun");
   },
}


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, AtLeast, 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
      Bring(P6, AtLeast, 1, "Any unit", "21.Magellan_Bozo");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(P6, SetTo, 1, " `SystemDebuff_Stun");
   },
}

for i = 0, 3, 1 do

radius = i / 4 * math.pi;

d = 50;

x = math.sin(radius) * d;
y = math.cos(radius) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

d2 = 100;

x2 = math.sin(radius) * d2;
y2 = math.cos(radius) * d2;
x2 = math.floor(x2 + 0.5);
y2 = math.floor(y2 + 0.5);


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 2 * i + 1, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", CurrentPlayer);
   },
}

Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Switch("Unique - Magellan", Set);
      Deaths(CurrentPlayer, Exactly, 2 * i + 2, " `UniqueSkill");
      Deaths(CurrentPlayer, Exactly, 320, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillWait");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      CreateUnit(2, "60 + 1n Archon", "[Skill]Unit_Wait_8", CurrentPlayer);
      CreateUnit(2, "60 + 1n Danimoth", "[Skill]Unit_Wait_8", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, x2, y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      LMove(179, -x2, -y2);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveUnit(1, "60 + 1n Danimoth", CurrentPlayer, "[Skill]Unit_Wait_ALL", "21.Magellan_Bozo");
      MoveLocation("21.Magellan_Bozo", "80 + 1n Tom Kazansky", CurrentPlayer, "Anywhere");
      Order("60 + 1n Danimoth", CurrentPlayer, "Anywhere", Attack, "21. Magellan");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
   },
}

end


Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `UniqueSkill");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 9, " `UniqueSkill");
   },
}



Trigger { -- Skill : S
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 1000, " * Probe");
      Bring(CurrentPlayer, AtLeast, 1, " * Probe", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 2, " `UniqueSkill");
   },
   actions = {
      Comment("Skill : Unique");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Subtract, 1, " `UniqueSkill");
   },
}





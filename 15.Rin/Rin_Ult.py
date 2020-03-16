Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("15.Rin_Bozo", " * Devouring One", CurrentPlayer, "Anywhere");
      ModifyUnitShields(All, " * Devouring One", CurrentPlayer, "Anywhere", 1);
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, AtLeast, 2, " `SkillCount");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "Target", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin_Bozo", " * Devouring One", CurrentPlayer, "Anywhere");
      MoveUnit(1, "Target", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin_Bozo");
      RemoveUnitAt(All, "Target", "Anywhere", CurrentPlayer);
      Order(" * Devouring One", CurrentPlayer, "Anywhere", Move, "15.Rin_Bozo");
   },
}

Trigger { -- Skill : Use Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop4");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveUnit(All, "40 + 1n Mojo", CurrentPlayer, "Anywhere", "[Skill]HoldPosition");
      MoveUnit(All, "40 + 1n Mojo", P12, "Anywhere", "[Skill]HoldPosition");
      MoveUnit(All, "40 + 1n Mojo", P11, "Anywhere", "[Skill]HoldPosition");
   },
}


for i = 0, 3, 1 do

radius1 = (i * 2 + 1) / 8 * math.pi;

d = 80 + 80 * i;

x = math.sin(radius1) * d;
y = math.cos(radius1) * d;
x = math.floor(x + 0.5);
y = math.floor(y + 0.5);

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtMost, 8, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "15.Rin");
      Wait(100);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, AtLeast, 9, " `SkillLoop");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(4, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, x, y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -x, -y);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, -y, x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      LMove(165, y, -x);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "15.Rin");
      Wait(100);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}
end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Bring(CurrentPlayer, AtLeast, 1, "60 + 1n Siege", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", "60 + 1n Siege", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(2, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(1, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "15.Rin");
      RemoveUnitAt(All, "40 + 1n Mojo", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Bring(CurrentPlayer, AtLeast, 1, "100 + 1n Dragoon", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", "100 + 1n Dragoon", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "100 + 1n Dragoon", "Anywhere", CurrentPlayer);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(2, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(1, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "15.Rin");
      RemoveUnitAt(All, "40 + 1n Mojo", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Bring(CurrentPlayer, AtLeast, 1, "60 + 1n High Templar", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", "60 + 1n High Templar", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(2, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(1, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "15.Rin");
      RemoveUnitAt(All, "40 + 1n Mojo", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop3");
      Bring(CurrentPlayer, AtLeast, 1, "60 + 1n Dragoon", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(2, "40 + 1n Mojo", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", "60 + 1n Dragoon", CurrentPlayer, "Anywhere");
      KillUnitAt(1, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(2, "40 + 1n Mojo", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      KillUnitAt(1, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "15.Rin");
      RemoveUnitAt(All, "40 + 1n Mojo", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillLoop2");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 18, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop2");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop3");
      Wait(200);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "15.Rin");
      Wait(1400);
      GiveUnits(All, "40 + 1n Mojo", CurrentPlayer, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
      Wait(550);
      GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
      Wait(2050);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop4");
      Wait(900);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 2, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 1, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Move, "15.Rin");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 3, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
      Wait(1620);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop4");
      Wait(1700);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
      GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}

for i = 0, 31, 1 do


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop3");
      Bring(P12, AtLeast, 1, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "60 + 1n Siege", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", "40 + 1n Mojo", P12, "Anywhere");
      GiveUnits(1, "40 + 1n Mojo", P12, "Anywhere", P11);
      MoveUnit(1, "60 + 1n Siege", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 32, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Bring(P12, Exactly, 0, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Siege", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 4, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(1500);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop4");
      Wait(1050);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
      GiveUnits(All, "40 + 1n Mojo", P11, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}


for i = 0, 31, 1 do


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop3");
      Bring(P12, AtLeast, 1, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "60 + 1n Dragoon", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", "40 + 1n Mojo", P12, "Anywhere");
      GiveUnits(1, "40 + 1n Mojo", P12, "Anywhere", P11);
      MoveUnit(1, "60 + 1n Dragoon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 32, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Dragoon", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Bring(P12, Exactly, 0, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n Dragoon", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 5, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(1500);
      SetDeaths(CurrentPlayer, SetTo, 1, " `SkillLoop4");
      Wait(1400);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop4");
      GiveUnits(All, "40 + 1n Mojo", P11, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}


for i = 0, 31, 1 do


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop3");
      Bring(P12, AtLeast, 1, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "60 + 1n High Templar", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", "40 + 1n Mojo", P12, "Anywhere");
      GiveUnits(1, "40 + 1n Mojo", P12, "Anywhere", P11);
      MoveUnit(1, "60 + 1n High Templar", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 32, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n High Templar", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Bring(P12, Exactly, 0, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      RemoveUnitAt(All, "60 + 1n High Templar", "[Skill]Unit_Wait_ALL", CurrentPlayer);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 6, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(2000);
      GiveUnits(All, "40 + 1n Mojo", P11, "Anywhere", P7);
      GiveUnits(All, "40 + 1n Mojo", P12, "Anywhere", P7);
      SetSwitch("JunkYardDog", Set);
      Wait(0);
      SetSwitch("JunkYardDog", Clear);
      GiveUnits(All, "40 + 1n Mojo", P7, "Anywhere", P12);
      RemoveUnitAt(All, "40 + 1n Mojo", "[Skill]Unit_Wait_ALL", P11);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}

for i = 0, 31, 1 do


Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, i, " `SkillLoop3");
      Bring(P12, AtLeast, 1, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      CreateUnit(1, "60 + 1n Archon", "[Skill]Unit_Wait_1", CurrentPlayer);
      CreateUnit(1, "Kakaru (Twilight)", "[Skill]Unit_Wait_1", CurrentPlayer);
      SetInvincibility(Enable, "Any unit", CurrentPlayer, "[Skill]Unit_Wait_ALL");
      MoveLocation("15.Rin", "40 + 1n Mojo", P12, "Anywhere");
      GiveUnits(1, "40 + 1n Mojo", P12, "Anywhere", CurrentPlayer);
      MoveUnit(1, "60 + 1n Archon", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      MoveUnit(1, "Kakaru (Twilight)", CurrentPlayer, "[Skill]Unit_Wait_ALL", "15.Rin");
      SetDeaths(CurrentPlayer, Add, 1, " `SkillLoop3");
   },
}

end

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 32, " `SkillLoop3");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "15.Rin");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Bring(P12, Exactly, 0, "40 + 1n Mojo", "Anywhere");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      KillUnitAt(All, "60 + 1n Archon", "Anywhere", CurrentPlayer);
      KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", CurrentPlayer);
      MoveLocation("15.Rin", " * Devouring One", CurrentPlayer, "Anywhere");
      Order("40 + 1n Mojo", CurrentPlayer, "Anywhere", Attack, "15.Rin");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop3");
   },
}

Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 7, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(1600);
      SetDeaths(CurrentPlayer, Add, 1, " `SkillCount");
   },
}



Trigger { -- Skill : Combo
   players = {Force1, Force2},
   conditions = {
      Deaths(CurrentPlayer, Exactly, 2000, " * Devouring One");
      Bring(CurrentPlayer, AtLeast, 1, " * Devouring One", "Anywhere");
      Deaths(CurrentPlayer, Exactly, 310, " `SkillStep");
      Deaths(CurrentPlayer, Exactly, 8, " `SkillCount");
      Deaths(CurrentPlayer, Exactly, 0, " `SkillLoop");
   },
   actions = {
      Comment("Skill : Ultimate");
      PreserveTrigger();
      Wait(5400);
      KillUnitAt(All, "60 + 1n High Templar", "Anywhere", CurrentPlayer);
      Wait(2200);
      KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", CurrentPlayer);
      Wait(3000);
      KillUnitAt(All, "40 + 1n Mojo", "Anywhere", CurrentPlayer);
      Wait(3000);
      KillUnitAt(All, "60 + 1n Siege", "Anywhere", CurrentPlayer);
      SetSwitch("Recall - Rin", Clear);
      Wait(500);
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillCount");
      SetDeaths(CurrentPlayer, SetTo, 0, " `SkillLoop");
      SetDeaths(CurrentPlayer, Add, 12, " `SkillWait");
   },
}


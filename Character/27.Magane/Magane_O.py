import Function as f;

function main(cp)
{
   MoveLocation("27.Magane_Bozo", f.heroID[cp], cp, "Anywhere");

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {
            f.EdgeShape(cp, 1, "40 + 1n Guardian", 45, 3, 50);
            f.EdgeShape(cp, 1, "Protoss Dark Archon", 45, 3, 50);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
         }
         else if (f.loop[cp] == 2)
         {
            f.EdgeShape(cp, 1, "Kakaru (Twilight)", 45, 3, 50);
            f.EdgeShape(cp, 1, " Unit. Hoffnung 25000", 45, 3, 50);
            KillUnitAt(All, "Kakaru (Twilight)", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);
         }

         f.SkillWait(cp, 80);

         f.loop[cp] += 1;

         if (f.loop[cp] == 16)
         {
            f.Voice_Routine(cp, 9);
            SetSwitch("Recall - Magane", Set);

            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 1)
      {
         if (Switch("UiltimateSwitch", Cleared))
         {
            if (cp < 3)
            {
               GiveUnits(All, "Protoss Dark Templar", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Marine", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Ghost", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Vulture", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Goliath", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Wraith", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Firebat", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Zergling", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, " Creep. Licht", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Drone", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Mutalisk", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Guardian", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Zealot", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 3n Zeratul", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Mojo", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Gantrithor", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "40 + 1n Lurker", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "50 + 1n Tank", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "50 + 1n Battlecruiser", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "60 + 3n Siege", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "60 + 1n Siege", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "60 + 1n Hydralisk", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "60 + 1n Dragoon", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "60 + 1n High Templar", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "60 + 1n Archon", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "60 + 1n Danimoth", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "60 + 3n Ghost", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Goliath", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Vulture", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Marine", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Tom Kazansky", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Tank", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Mutalisk", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Guardian", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Artanis", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "80 + 1n Ghost", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "100 + 1n Hyperion", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "100 + 1n Dragoon", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "120 + 1n Archon", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "130 + 1n Norad", Foes, "27.Magane_Bozo", P7);
               GiveUnits(All, "130 + 1n Arbiter", Foes, "27.Magane_Bozo", P7);
            }
            if (cp >= 3)
            {
               GiveUnits(All, "Protoss Dark Templar", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Marine", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Ghost", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Vulture", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Goliath", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Wraith", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Firebat", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Zergling", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, " Creep. Licht", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Drone", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Mutalisk", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Guardian", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Zealot", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 3n Zeratul", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Mojo", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Gantrithor", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "40 + 1n Lurker", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "50 + 1n Tank", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "50 + 1n Battlecruiser", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "60 + 3n Siege", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "60 + 1n Siege", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "60 + 1n Hydralisk", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "60 + 1n Dragoon", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "60 + 1n High Templar", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "60 + 1n Archon", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "60 + 1n Danimoth", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "60 + 3n Ghost", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Goliath", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Vulture", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Marine", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Tom Kazansky", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Tank", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Mutalisk", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Guardian", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Artanis", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "80 + 1n Ghost", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "100 + 1n Hyperion", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "100 + 1n Dragoon", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "120 + 1n Archon", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "130 + 1n Norad", Foes, "27.Magane_Bozo", P8);
               GiveUnits(All, "130 + 1n Arbiter", Foes, "27.Magane_Bozo", P8);
            }

         }

         f.SkillWait(cp, 80);

         if (f.loop[cp] == 19)
         {
            f.Voice_Routine(cp, 10);
         }

         f.loop[cp] += 1;

         if (f.loop[cp] == 46)
         {
            f.count[cp] += 1;
            f.loop[cp] = 0;         
         }
      }
      else if (f.count[cp] == 2)
      {
         KillUnitAt(All, "Protoss Dark Templar", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Goliath", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Vulture", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Marine", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Tank", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Guardian", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Artanis", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Ghost", "Anywhere", P7);
         KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", P7);
         KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", P7);
         KillUnitAt(All, "120 + 1n Archon", "Anywhere", P7);
         KillUnitAt(All, "130 + 1n Norad", "Anywhere", P7);
         KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Marine", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", P7);
         KillUnitAt(All, "80 + 1n Vulture", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Firebat", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Zergling", "Anywhere", P7);
         KillUnitAt(All, " Creep. Licht", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Zealot", "Anywhere", P7);
         KillUnitAt(All, "40 + 3n Zeratul", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", P7);
         KillUnitAt(All, "40 + 1n Lurker", "Anywhere", P7);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", P7);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", P7);
         KillUnitAt(All, "60 + 3n Siege", "Anywhere", P7);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", P7);
         KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", P7);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", P7);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", P7);
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", P7);
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", P7);
         KillUnitAt(All, "60 + 3n Ghost", "Anywhere", P7);

         KillUnitAt(All, "Protoss Dark Templar", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Goliath", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Vulture", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Marine", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Tom Kazansky", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Tank", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Mutalisk", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Guardian", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Artanis", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Ghost", "Anywhere", P8);
         KillUnitAt(All, "100 + 1n Hyperion", "Anywhere", P8);
         KillUnitAt(All, "100 + 1n Dragoon", "Anywhere", P8);
         KillUnitAt(All, "120 + 1n Archon", "Anywhere", P8);
         KillUnitAt(All, "130 + 1n Norad", "Anywhere", P8);
         KillUnitAt(All, "130 + 1n Arbiter", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Marine", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Ghost", "Anywhere", P8);
         KillUnitAt(All, "80 + 1n Vulture", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Goliath", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Firebat", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Zergling", "Anywhere", P8);
         KillUnitAt(All, " Creep. Licht", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Drone", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Mutalisk", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Guardian", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Zealot", "Anywhere", P8);
         KillUnitAt(All, "40 + 3n Zeratul", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Gantrithor", "Anywhere", P8);
         KillUnitAt(All, "40 + 1n Lurker", "Anywhere", P8);
         KillUnitAt(All, "50 + 1n Tank", "Anywhere", P8);
         KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", P8);
         KillUnitAt(All, "60 + 3n Siege", "Anywhere", P8);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", P8);
         KillUnitAt(All, "60 + 1n Hydralisk", "Anywhere", P8);
         KillUnitAt(All, "60 + 1n Dragoon", "Anywhere", P8);
         KillUnitAt(All, "60 + 1n High Templar", "Anywhere", P8);
         KillUnitAt(All, "60 + 1n Archon", "Anywhere", P8);
         KillUnitAt(All, "60 + 1n Danimoth", "Anywhere", P8);
         KillUnitAt(All, "60 + 3n Ghost", "Anywhere", P8);

         SetSwitch("Recall - Magane", Clear);
         SetDeaths(cp, SetTo, 1080, " `UniqueCoolTime");

         f.SkillEnd(cp);
      }
   }
}


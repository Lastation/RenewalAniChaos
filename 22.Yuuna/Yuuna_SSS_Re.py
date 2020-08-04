import Function as f;

const s = StringBuffer();

function main(cp, location, heroID)
{
   f.loop[cp] = dwread_epd(212 * 12 + cp);
   f.count[cp]  = dwread_epd(181 * 12 + cp);

   if (Deaths(cp, Exactly, 0, " `WaitTime"))
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] == 0)
         {                        
            f.NxNSquareShape(heroID, 1, "40 + 1n Wraith", location, cp, 3, 75);
            f.NxNSquareShape(heroID, 1, " Unit. Hoffnung 25000", location, cp, 3, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 1)
         {
            f.NxNSquareShape(heroID, 1, "40 + 1n Wraith", location, cp, 5, 75);
            f.NxNSquareShape(heroID, 1, " Unit. Hoffnung 25000", location, cp, 5, 75);
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
            KillUnitAt(All, " Unit. Hoffnung 25000", "Anywhere", cp);

            f.SkillWait(cp, 80);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 2)
         {
            f.NxNSquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 3, 75);
            Order("50 + 1n Battlecruiser", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 80);

            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 3)
         {
            f.SquareShape(heroID, 1, "Protoss Dark Archon", location, cp, 150, 150);
            f.SquareShape(heroID, 1, "Protoss Dark Archon", location, cp, 150, 75);
            f.SquareShape(heroID, 1, "Protoss Dark Archon", location, cp, 150, 0);
            f.SquareShape(heroID, 1, "Protoss Dark Archon", location, cp, 150, -75);
            f.SquareShape(heroID, 1, "40 + 1n Guardian", location, cp, 150, 150);
            f.SquareShape(heroID, 1, "40 + 1n Guardian", location, cp, 150, 75);
            f.SquareShape(heroID, 1, "40 + 1n Guardian", location, cp, 150, 0);
            f.SquareShape(heroID, 1, "40 + 1n Guardian", location, cp, 150, -75);
            KillUnitAt(All, "40 + 1n Guardian", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] < 4)
         {         
            f.SquareShape(heroID, 1, "Protoss Dark Archon", location, cp, 150, 150 - 75 * f.loop[cp]);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);

            f.SkillWait(cp, 80);
            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 4)
         {
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);

            f.SkillWait(cp, 80);

            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 5)
         {
            f.SquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 150, 150);
            f.SquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 150, 75);
            f.SquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 150, 0);
            f.SquareShape(heroID, 1, "50 + 1n Battlecruiser", location, cp, 150, -75);
            f.SquareShape(heroID, 1, "50 + 1n Tank", location, cp, 150, 150);
            f.SquareShape(heroID, 1, "50 + 1n Tank", location, cp, 150, 75);
            f.SquareShape(heroID, 1, "50 + 1n Tank", location, cp, 150, 0);
            f.SquareShape(heroID, 1, "50 + 1n Tank", location, cp, 150, -75);
            KillUnitAt(All, "50 + 1n Battlecruiser", "Anywhere", cp);
            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);

            f.SkillWait(cp, 80);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }
      }


      else if (f.count[cp] == 2)
      {
         if (f.loop[cp] == 0)
         {
            f.SquareShape(heroID, 1, "40 + 1n Mojo", location, cp, 100, 100);
            f.SquareShape(heroID, 1, "40 + 1n Mojo", location, cp, 100, 50);
            f.SquareShape(heroID, 1, "40 + 1n Mojo", location, cp, 100, 0);
            f.SquareShape(heroID, 1, "40 + 1n Mojo", location, cp, 100, -50);
            f.SquareShape(heroID, 1, "60 + 1n Archon", location, cp, 100, 100);
            f.SquareShape(heroID, 1, "60 + 1n Archon", location, cp, 100, 50);
            f.SquareShape(heroID, 1, "60 + 1n Archon", location, cp, 100, 0);
            f.SquareShape(heroID, 1, "60 + 1n Archon", location, cp, 100, -50);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            MoveLocation(location, heroID, cp, "Anywhere");
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, location);

            f.SkillWait(cp, 160);

            SetDeaths(cp, Add, 1, " `SkillLoop");
         }
         else if (f.loop[cp] == 1)
         {
            KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

            f.NxNSquareShape(heroID, 1, "40 + 1n Mojo", location, cp, 3, 50);
            f.NxNSquareShape(heroID, 1, "60 + 1n Archon", location, cp, 3, 50);
            KillUnitAt(All, "60 + 1n Archon", "Anywhere", cp);
            Order("40 + 1n Mojo", cp, "Anywhere", Attack, "Anywhere");

            f.SkillWait(cp, 160);

            SetDeaths(cp, Add, 1, " `SkillCount");
            SetDeaths(cp, SetTo, 0, " `SkillLoop");
         }
      }
      else if (f.count[cp] == 3)
      {
         KillUnitAt(All, "40 + 1n Mojo", "Anywhere", cp);

         f.SkillEnd(cp);
      }
   }
}
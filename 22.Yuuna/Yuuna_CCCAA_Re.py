import Function as f;

const s = StringBuffer();

function main(cp)
{
   f.BanReturn(cp);
   f.HoldPosition(cp);

   if (f.delay[cp] == 0)
   {
      if (f.count[cp] == 0)
      {
         if (f.loop[cp] < 15)
         {         
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.MoveLoc(f.heroID[cp], cp, 200 - 50 * (f.loop[cp] % 4), 50 * (f.loop[cp] % 4));
            f.SkillUnit(cp, 1, "50 + 1n Tank");
            f.SkillUnit(cp, 1, "60 + 1n Danimoth");
            f.MoveLoc(f.heroID[cp], cp, -200 + 50 * (f.loop[cp] % 4), -50 * (f.loop[cp] % 4));
            f.SkillUnit(cp, 1, "50 + 1n Tank");
            f.SkillUnit(cp, 1, "60 + 1n Danimoth");
            f.MoveLoc(f.heroID[cp], cp, 50 * (f.loop[cp] % 4), -200 + 50 * (f.loop[cp] % 4));
            f.SkillUnit(cp, 1, "Protoss Dark Archon");
            f.MoveLoc(f.heroID[cp], cp, -50 * (f.loop[cp] % 4), 200 - 50 * (f.loop[cp] % 4));
            f.SkillUnit(cp, 1, "Protoss Dark Archon");

            KillUnitAt(All, "50 + 1n Tank", "Anywhere", cp);
            KillUnitAt(All, "Protoss Dark Archon", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("60 + 1n Danimoth", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 80);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 15)
         {
            RemoveUnitAt(All, "60 + 1n Danimoth", "Anywhere", cp);

            f.SkillWait(cp, 80);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
      }
      else if (f.count[cp] == 1)
      {
         if (f.loop[cp] == 0)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Zealot", 100, 0);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 100, 50);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 100, -50);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 150, 0);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 150, 50);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 150, -50);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 200, 0);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 200, 50);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 200, -50);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 100, 0);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 100, 50);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 100, -50);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 150, 0);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 150, 50);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 150, -50);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 200, 0);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 200, 50);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 200, -50);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SkillWait(cp, 240);

            f.loop[cp] += 1;
         }
         else if (f.loop[cp] == 1)
         {         
            KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);

            f.SquareShape(cp, 1, "40 + 1n Zealot", 100, 100);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 100, 150);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 100, 200);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 150, 100);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 150, 150);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 150, 200);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 200, 100);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 200, 150);
            f.SquareShape(cp, 1, "40 + 1n Zealot", 200, 200);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 100, 100);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 100, 150);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 100, 200);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 150, 100);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 150, 150);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 150, 200);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 200, 100);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 200, 150);
            f.SquareShape(cp, 1, "40 + 1n Wraith", 200, 200);
            KillUnitAt(All, "40 + 1n Zealot", "Anywhere", cp);
            MoveLocation(f.location[cp], f.heroID[cp], cp, "Anywhere");
            Order("40 + 1n Wraith", cp, "Anywhere", Attack, f.location[cp]);

            f.SkillWait(cp, 240);

            f.count[cp] += 1;
            f.loop[cp] = 0;
         }
         
      }
      else if (f.count[cp] == 2)
      {

         KillUnitAt(All, "40 + 1n Wraith", "Anywhere", cp);
         KillUnitAt(All, "60 + 1n Siege", "Anywhere", cp);
         f.SkillEnd(cp);


      }


   }
}